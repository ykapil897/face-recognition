# Face-Recognition
**Face-Recognition on Labelled Faces in the Wild**

[project page](https://ykapil897.github.io/face-recognition/) | [Report](https://github.com/ykapil897/face-recognition/Report/Report.pdf)

## Requirements
* Use **python >= 3.8.16**. Conda recommended : [https://docs.anaconda.com/anaconda/install/linux/](https://docs.anaconda.com/anaconda/install/linux/)

* Use **pytorch 1.13.1 CUDA 11.6**
* Other requirements from 'requirements.txt' 

## To setup environment
```
# create new env face-recognition
$ conda create -n face-recognition python=3.8.16
```


# activate face-recognition
$ conda activate face-recognition

$ pip install -r requirements.txt

## Preparing dataset
- Download Labelled Faces in the Wild (LFW) dataset from [Kaggle](https://www.kaggle.com/datasets/jessicali9530/lfw-dataset)

Store the downloaded dataset in the `./data/` directory.

## If you want you can use and check the directly the [Demo Code](https://ykapil897.github.io/face-recognition/demo_code_prediction.html)

## BibTex
<div style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
  <pre>
  @InProceedings{cstbir2024aaai,
        author    = {Sapkal, Vivek and Yadav, Kapil and Arsewad, Bagwan and Gavankar, Heramb and Patel, Raj and Suhani and Jateen},
        title     = {Face Recognition on Labelled Faces in the Wild (Dataset)},
        refs      = {<a href="https://www.analyticsvidhya.com/blog/2019/09/feature-engineering-images-introduction-hog-feature-descriptor/"> To understand hog </a>, 
        <a href="http://neuralnetworksanddeeplearning.com/chap2.html"> To understand backpropagation </a>, <a href="https://medium.com/swlh/local-binary-pattern-algorithm-the-math-behind-it-%EF%B8%8F-edf7b0e1c8b3"> To understand LBP </a>}
        year      = {2024},
    }      
  </pre>
</div>

## Acknowledgment
We would like to express my sincere gratitude to Anand Mishra, Assitant Professor, for this course project .
