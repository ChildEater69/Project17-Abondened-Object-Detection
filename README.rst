Project 17: Abandoned Object Detection - Day 1
===============================================

Welcome to Project 17 of my "25 Projects in 100 Days" series! This project is dedicated to my friend Vansh Aggarwal, who has been instrumental in providing guidance and inspiration. Together, we are embarking on the exciting journey of developing an abandoned object detection system using computer vision techniques.

.. image::
    :target: https://www.linkedin.com/in/avdhesh-kumar-sharma-751a49225
[Avdhesh Kumar Sharma's LinkedIn](https://www.linkedin.com/in/avdhesh-kumar-sharma-751a49225/)
[Vansh Aggarwal's LinkedIn](https://www.linkedin.com/in/vansh-aggarwal-531a6124a/)


Overview
--------

The goal of this project is to create an algorithm that can analyze video footage and identify objects left unattended for a certain period. By leveraging the power of OpenCV and various computer vision techniques, we aim to develop a robust and accurate abandoned object detection system.

Day 1 Progress
--------------

On Day 1, we laid the foundation for the project and made significant progress. Here are the key highlights:

1. Researched and gathered inspiration from expert resources in the field.
2. Collaborated with Vansh Agarwal to define the project's objectives and scope.
3. Imported essential libraries, including `numpy`, `cv2`, `Counter`, and `defaultdict`, to support our implementation.
4. Preprocessed the first frame of the video by converting it to grayscale and applying a Gaussian blur for noise reduction.
5. Created windows using `cv2.namedWindow()` to visualize the different stages of the algorithm, such as Canny edge detection and morphological closing.
6. Implemented a main processing loop to read each frame, analyze contours, and track potential abandoned objects based on centroids and consecutive appearances.
7. Annotated and marked detected abandoned objects on the video frames for better visualization.

Next Steps
----------

Although we have made good progress, there is still room for improvement. Here's what we plan to do next:

1. Refine the algorithm to enhance the accuracy of abandoned object detection.
2. Optimize the performance for real-time or near real-time processing.
3. Explore additional computer vision techniques to further improve the system's capabilities.
4. Document the code, add comments, and ensure readability for future reference.

We are excited about the potential of this project and look forward to further advancements. Join us on this journey as we continue to develop and refine our abandoned object detection system!

Get Involved
------------

Feel free to check out the code on our GitHub repository and leave your feedback or suggestions. Contributions are welcome!

GitHub: [Insert GitHub link]

Let's revolutionize surveillance and security through the power of computer vision! Together, we can make a difference.
