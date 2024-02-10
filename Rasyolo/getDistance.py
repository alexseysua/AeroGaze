

def GetDistance(box, frame_dim, gsd):
    middle_frame = (frame_dim[0]//2, frame_dim[1]//2)
    middle_box = box

    distx = abs(middle_frame[0]-middle_box[0])
    disty = abs(middle_box[1]-middle_frame[1])
    distx = distx*gsd[1]
    disty = disty*gsd[0]

    ph_end_x , ph_end_y = frame_dim[0], frame_dim[1]
    quad_1_dis = (((middle_box[0]-ph_end_x)**2)+((middle_box[1])**2))**(0.5)
    quad_2_dis = (((middle_box[0])**2)+((middle_box[1])**2))**(0.5)
    quad_3_dis = (((middle_box[0])**2)+((middle_box[1]-ph_end_y)**2))**(0.5)
    quad_4_dis = (((middle_box[0]-ph_end_x)**2)+((middle_box[1]-ph_end_y)**2))**(0.5)

    dis_lst=[]
    dis_lst.append(quad_1_dis)
    dis_lst.append(quad_2_dis)
    dis_lst.append(quad_3_dis)
    dis_lst.append(quad_4_dis)


    # val = dis_lst.index(min(dis_lst))
    if min(dis_lst) == quad_1_dis:
        quad = 'Quadrant 1'
        return disty, 0, distx, 0 ,quad   
    elif min(dis_lst) == quad_2_dis:      
        quad = 'Quadrant 2'
        return disty, 0, 0, distx, quad
    elif min(dis_lst) == quad_3_dis:   
        quad = 'Quadrant 3'
        return 0, disty, 0, distx, quad
    elif min(dis_lst) == quad_4_dis:
        quad = 'Quadrant 4'
        return 0, disty, distx, 0, quad

    # return quad, dis_lst, distx, disty