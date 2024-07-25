import sys
sys.path.append('../openpose/build/python/openpose')

import os
import cv2
import pyopenpose as op

def is_limb_missing(keypoints, limb_points):
    # 检查关键点是否存在
    for point in limb_points:
        if keypoints[point, 2] == 0:  # 置信度为0表示关键点不存在
            return True
    return False

def process_image(image_path, opWrapper):
    datum = op.Datum()
    imageToProcess = cv2.imread(image_path)
    datum.cvInputData = imageToProcess
    opWrapper.emplaceAndPop(op.VectorDatum([datum]))

    keypoints = datum.poseKeypoints

    if keypoints is not None and len(keypoints) > 0:
        for person in keypoints:
            # 定义四肢的关键点索引（左臂，右臂，左腿，右腿）
            left_arm_points = [5, 6, 7]
            right_arm_points = [2, 3, 4]
            left_leg_points = [11, 12, 13]
            right_leg_points = [8, 9, 10]

            # 检查每条四肢是否残缺
            left_arm_missing = is_limb_missing(person, left_arm_points)
            right_arm_missing = is_limb_missing(person, right_arm_points)
            left_leg_missing = is_limb_missing(person, left_leg_points)
            right_leg_missing = is_limb_missing(person, right_leg_points)

            if left_arm_missing or right_arm_missing or left_leg_missing or right_leg_missing:
                return True, datum.cvOutputData
        return False, datum.cvOutputData
    else:
        return None, None  # 没有检测到人物

def main():
    params = {
        "model_folder": "../openpose/models/"
    }

    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()

    input_folder = "./sample/"  # 确保这个文件夹存在且包含要处理的图像
    output_folder = "./output/"
    os.makedirs(output_folder, exist_ok=True)
    results = {}

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(input_folder, filename)

            result, render_image = process_image(image_path, opWrapper)
            if result is None:
                results[filename] = "未检测到人物"
            elif result:
                results[filename] = "四肢残缺"
            else:
                results[filename] = "四肢完好"

            if render_image is not None:
                save_render_image_file = output_folder + filename
                cv2.imwrite(save_render_image_file, render_image)

    for image, result in results.items():
        print(f"{image}: {result}")

if __name__ == "__main__":
    main()
