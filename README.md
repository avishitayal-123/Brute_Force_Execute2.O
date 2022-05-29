# Brute_Force_Execute2.O

## STEP : 1 - Mediapipe Body Detection:
**If we have full body image of a Model, the face with hands and cordinates of the shoulders must be recorded, we will be using Mediapipe full body detection for this Module**
<p float="left"> 
<img src="https://user-images.githubusercontent.com/94181768/170849835-b6a42757-5011-4641-92db-6824f182dc2b.png" width="30%" height="30%"/>
<img src="https://user-images.githubusercontent.com/94181768/170849838-582d1a76-96b9-45cf-af44-66d1447d8f00.png" width="25%" height="25%"/>
<img src="https://user-images.githubusercontent.com/94181768/170849932-a768c995-040b-4880-8c61-ecb08d35c7e0.png" width="27.5%" height="27.5%"/>
</p>

## STEP : 2 - Clothes Segmentation:
**We have 2 Models for this Segmentation task. One is a Pre - Trained Model and other is a Self Trained Module which we have trained on the dataset extracted from Myntra Website using the code Downloaded-Image-Myntra**
- Link to the Dataset : - https://drive.google.com/file/d/1jUYJHOr8PzCzlOvXvlgZbZtV2gnpQHfO/view?usp=sharing
- Link to the Checkpoints : - https://drive.google.com/file/d/1RGDLcCUFljd6Vmmx5IpHH-KNzLrZ9MnG/view?usp=sharing
<p float = "left">
  <img src="https://user-images.githubusercontent.com/94181768/170849932-a768c995-040b-4880-8c61-ecb08d35c7e0.png" width="30%" height="30%"/>
  <img src = "https://user-images.githubusercontent.com/94181768/170850385-59bc3538-67d9-4ef8-bb82-149b24b5eb46.png" width="27%" height="27%"/>
</p>

**Our accuracy on complex postures** 

<p float = "left">
  <img src="https://user-images.githubusercontent.com/94181768/170850898-3c741776-2da7-4732-adee-2bdc7ec70e5f.jpg" width="27%" height="20%"/>
  <img src = "https://user-images.githubusercontent.com/94181768/170850923-a7aea94d-8ae1-4599-ad85-56546d879414.png" width="30%" height="45%"/>
</p>

## STEP : 3 - Clothes Segmentation:

## K-Means Cluster:

**As we have the front image of the cloth using mediapipe, so with a view to have the backside of the 3D image of cloth we use K-means cluster. 
Here it can generate backside of three types of clothes- T shirt, shorts and trouser.** 


![Tshirt](Tshirt.png)
![Shorts](Shorts.png)
![Colour map](Colour_map.png)
