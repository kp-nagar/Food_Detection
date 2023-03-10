from PIL import Image
from io import BytesIO
import base64

import torch
from torchvision import transforms


def predict_class(image_base64_data):

    __model = torch.jit.load('models/succ_300_data_aug_128px.pt')

    pil_img = get_image_from_base64_string(image_base64_data)

    data_transform = transforms.Compose([transforms.Resize(size=(128, 128)),transforms.ToTensor()])
    transformed_img = data_transform(pil_img).unsqueeze(dim=0)

    with torch.inference_mode():
        custom_image_pred = __model(transformed_img)

    custom_image_pred = torch.softmax(custom_image_pred, dim=1)

    decode = ['Chai', 'Jalebi', 'Samosa']
    custom_image_pred_list = [round(i, 2) * 100 for i in custom_image_pred[0].tolist()]
    class_pred_perc = {k:v for k,v in zip(decode, custom_image_pred_list) }
    print(class_pred_perc)

    high_prob_index = custom_image_pred_list.index(max(custom_image_pred_list))
    max_prob_per = max(custom_image_pred_list)

    print("Max probability %.2f" % max_prob_per + '%')

    if max_prob_per >= 85:
        predict_img = decode[high_prob_index]
    elif 60 <= max_prob_per < 85:
        predict_img = f"Probability is low({max_prob_per}) but let's check it's: {decode[high_prob_index]}"
    else:
        print("Not detect")
        predict_img = "We will support complex images in our next version. Thanks!"

    return {'class': predict_img}


def get_image_from_base64_string(b64str):
    '''
    credit: https://stackoverflow.com/questions/26070547/decoding-base64-from-post-to-use-in-pil
    '''
    encoded_image = b64str.split(',')[1]
    return Image.open(BytesIO(base64.b64decode(encoded_image)))
