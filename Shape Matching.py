import cv2

image = cv2.imread('Shape.jpg',0)

ret,thresh = cv2.threshold(image,127,255,1)




imageN, contours, hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
print len(contours)

n=len(contours)-1
contours = sorted(contours,key=cv2.contourArea,reverse=False)[:n]

for c in contours:
    epsilon = 0.01 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    print len(approx )
    if len(approx)==3:
        shape_name = "Triangle"
        cv2.drawContours(thresh,[c],0,(255,255,255),-1)
        # Finding Moments
        M = cv2.moments(c)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.putText(thresh,shape_name,(cx-45,cy),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)


    elif len(approx)==4:
        x,y,w,h=cv2.boundingRect(c)
        M = cv2.moments(c)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])

        if w-h>=4:
            shape_name="Square"
            cv2.drawContours(thresh, [c], 0, (255,255,255), -1)
            cv2.putText(thresh, shape_name, (cx - 45, cy), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 1)
        else:
            shape_name = "Rectangle"
            cv2.drawContours(thresh, [c], 0, (255,255,255), -1)
            cv2.putText(thresh, shape_name, (cx - 45, cy), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 1)

    elif len(approx)==10:
        shape_name = "Star"
        cv2.drawContours(thresh, [c], 0, (255,255,255), -1)
        # Finding Moments
        M = cv2.moments(c)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.putText(thresh, shape_name, (cx - 45, cy), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 1)


    elif len(approx)>=15:
        shape_name = "Circle"
        cv2.drawContours(thresh, [c], 0, (255,255,255), -1)
        # Finding Moments
        M = cv2.moments(c)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.putText(thresh , shape_name, (cx - 45, cy), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 1)

    cv2.imshow("Shapes", thresh)
    cv2.waitKey(0)



cv2.destroyAllWindows()