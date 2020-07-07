import json
import cv2
'''
    I think this badboy could work as a semi-manual-labeler, this crop 2 areas
    from death scoreboard and allow you to label it in a 'black magic switch
    logic' way that is not ok.

    @Author: SERGI

'''


diccionario = {}

video_rgb = cv2.VideoCapture('./resources/videoHD.mp4')
video_rgb.set(cv2.CAP_PROP_POS_FRAMES, (30*30)-1)


_, frame = video_rgb.read()
h = frame.shape[0]
w = frame.shape[1]
h1 = int(h/33)
w1 = int(w - w/5.40)
fp = 0
frames_red = []
frames_blue = []
imagesRed = []
imagesBlue = []
while(video_rgb.isOpened()):

    # Capture frame-by-frame
    ret, frame = video_rgb.read()
    fp += 300
    # ret == false and end video happns
    if (ret):

    # ========================================================================
    # U are looking for this shit, good luck in CROP CITY
    # ========================================================================

        frame = frame[0:h1, w1:w1+43]
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_red = frame[7:len(frame)-7, :12]
        frame_blue = frame[7:len(frame)-7, len(frame[0])-12: len(frame[0])]

        add_red = True
        add_blue = True
        '''
        for image in imagesRed:
            if(np.all(image==frame_red)):
                add_red=False
                break

        for image in imagesBlue:
            if(np.all(image==frame_blue)):
                add_blue=False
                break
        '''
        if (add_red):
            frames_red.append(frame_red)
            imagesRed.append(frame_red.tolist())
        if (add_blue):
            frames_blue.append(frame_blue)
            imagesBlue.append(frame_blue.tolist())

        # cv2.imshow("frame",frame_red)
        video_rgb.set(cv2.CAP_PROP_POS_FRAMES, (fp*30)-1)
    else:
        break
diccionario["featuresBlue"] = imagesBlue
diccionario["featuresRed"] = imagesRed

# index=np.arange(len(imagesBlue))
# for idx,image in enumerate(imagesBlue):

#     cv2.imwrite("./dataaa/blue/"+str(index[idx])+".jpg", image)

# index=np.arange(len(imagesRed))
# for idx,image in enumerate(imagesRed):

# cv2.imwrite("./dataaa/red/"+str(index[idx])+".jpg", image)
index = 0
labels = []
for img in frames_red:

    cv2.imshow('img', img)
    k = cv2.waitKey()
    if k == 27:    # Esc key to stop
        break
    # p
    elif k == 112:

        labels.append(None)
        index += 1
    elif k == -1:  # normally -1 returned,so don't print it
        continue
    # b
    elif k == 98:  # ir atras un numero, actualizarlo, escribir este y continua
        cv2.imshow('Anterior', frames_red[index-1])
        q = cv2.waitKey()
        if q == 27:    # Esc key to stop
            break
        else:

            labels[-1] = q - 48
            print("rojos!! modficiado " + str(q-48))
            cv2.imshow('img', img)
            q = cv2.waitKey()
            print("rojos!! actual " + str(q-48))
            labels.append(q - 48)
    else:

        labels.append(k-48)
        index += 1
        print("rojos!! " + str(k-48))  # else print its value
    cv2.destroyAllWindows()
diccionario["LabelsRed"] = labels

index = 0
labels = []
for img in frames_blue:

    cv2.imshow('img', img)
    k = cv2.waitKey()
    if k == 27:    # Esc key to stop
        break

    elif k == -1:  # normally -1 returned,so don't print it
        continue

    elif k == 112:
        labels.append(None)
        index += 1

    elif k == 98:  # ir atras un numero, actualizarlo, escribir este y conti
        cv2.imshow('Anterior', frames_red[index-1])
        q = cv2.waitKey()
        if q == 27:    # Esc key to stop
            break
        else:
            labels[-1] = q - 48
            print("azul!! modficiado " + str(q-48))
            cv2.imshow('img', img)
            q = cv2.waitKey()
            labels.append(q - 48)
            print("azul!! actual " + str(q-48))
    else:

        labels.append(k-48)
        index += 1
        print("valuee!! " + str(k))  # else print its value

    cv2.destroyAllWindows()
diccionario["LabelsBlue"] = labels
with open("./dataaa/final_data_18x12_20samples.json", "w") as file:
    json.dump(diccionario, file)
