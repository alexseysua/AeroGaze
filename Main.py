from dronekit import connect, VehicleMode, LocationGlobalRelative
from Constants import connectionString, baudRate, speed, lAcc, AiSpeed, landingSpeed, altitude, conf, weight
from Drone.Drone import arm_and_takeoff, get_location_metres
from Camera.Camera import capture_image
import uuid
import time
import os
from Rasyolo.detect import run


try:
    # Making Connection
    vehicle = connect(connectionString, wait_ready=True, baud=baudRate)
    print("Vehicle Connected successfully...")

    # destlat = float(input())
    # destlong = float(input())
    destlat, destlong = map(float, input().split(", "))

    # Taking off
    if vehicle.mode.name != "GUIDED":
        vehicle.mode  = VehicleMode("GUIDED")
        
    arm_and_takeoff(vehicle, altitude)

    # Changing to Guided mode
    if vehicle.mode.name != "GUIDED":
        vehicle.mode  = VehicleMode("GUIDED")

    # Going to Destination
    dest_location = LocationGlobalRelative(destlat, destlong, altitude)
    vehicle.simple_goto(dest_location, groundspeed=speed)
    while vehicle.location.global_relative_frame.distance_to(dest_location) > 0.05:
        time.sleep(1)


    while True:
        # Capturing Image in Rasperry Pi
        capture_image("image.jpg")

        # Running Yolo
        # moving = yolo It will give (forwardDistance, backwardDistance, RollrightDistance, RollleftDistance)
        # decision = (0, 101.5, 0, 86.25, 'Quadrant 3')
        decision = run(weights=weight, source="image.jpg", conf_thres=conf)

        # Moving captured image to temp folder
        os.rename('image.jpg', f'temp/{str(uuid.uuid1())}.jpg')

        # Moving to helipad
        print("Controls taken by AI...")
        forwardLocation = get_location_metres(vehicle.location.global_relative_frame, decision[0], vehicle.heading)
        backwardLocation = get_location_metres(vehicle.location.global_relative_frame, decision[1], vehicle.heading)
        rightLocation = get_location_metres(vehicle.location.global_relative_frame, decision[2], vehicle.heading)
        leftLocation = get_location_metres(vehicle.location.global_relative_frame, decision[3], vehicle.heading)
        vehicle.simple_goto(forwardLocation, groundspeed=AiSpeed)
        # time.sleep(1)
        while vehicle.location.global_relative_frame.distance_to(dest_location) > 0.05:
            time.sleep(1)
        vehicle.simple_goto(backwardLocation, groundspeed=AiSpeed)
        # time.sleep(1)
        while vehicle.location.global_relative_frame.distance_to(dest_location) > 0.05:
            time.sleep(1)
        vehicle.simple_goto(rightLocation, groundspeed=AiSpeed)
        while vehicle.location.global_relative_frame.distance_to(dest_location) > 0.05:
            time.sleep(1)
        vehicle.simple_goto(leftLocation, groundspeed=AiSpeed)
        # time.sleep(1)
        while vehicle.location.global_relative_frame.distance_to(dest_location) > 0.05:
            time.sleep(1)
        # if moving[0]<lAcc and moving[1]<lAcc and moving[2]<lAcc and moving[3]<lAcc:
        if all(mov < lAcc for mov in decision[:4]):
            print("Correctly Aligned in the Helipad with accuracy", lAcc)
            break

    # Landing
    print("Landing...")
    vehicle.mode = VehicleMode("LAND", airspeed=landingSpeed)
    time.sleep(5)

    # Triggering actions like dropping..

    # Return to Launching pad
    print("Return to launch...")
    vehicle.mode = VehicleMode("RTL", groundspeed=speed, airspeed=landingSpeed)
    time.sleep(4)

    print("Landed safely...")
except Exception as e:
    print(f"Error:{e}")

finally:
    vehicle.close()