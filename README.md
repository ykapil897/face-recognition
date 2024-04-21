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

## Feel free to explore the [Demo Code](https://ykapil897.github.io/face-recognition/demo_code_prediction.html) directly.

## BibTex
<div style="border: 1px solid black; padding: 10px; background-color: #f0f0f0;">
    <pre>
@online{AnalyticaVidhya,
    author = "Aishwarya Singh",
    title = "Feature Engineering for Images: A Valuable Introduction to the HOG Feature Descriptor",
    url  = "https://www.analyticsvidhya.com/blog/2019/09/feature-engineering-images-introduction-hog-feature-descriptor/",
    addendum = "(accessed: 07.04.2024)",
    keywords = "latex,Hog,features"
}

@online{Medium_aricle,
    author = "Mahmoud Harmouch",
    title = "Local Binary Pattern Algorithm: The Math Behind It",
    url  = "https://medium.com/swlh/local-binary-pattern-algorithm-the-math-behind-it-%EF%B8%8F-edf7b0e1c8b3",
    addendum = "(accessed: 04.04.2024)",
    keywords = "latex,LocalBinaryPattern,featureExtraction"
}

@online{Neural_network,
    author = "Michael Nielsen",
    title = "How the backpropagation algorithm works",
    url  = "http://neuralnetworksanddeeplearning.com/chap2.html",
    addendum = "(accessed: 28.03.2024)",
    keywords = "latex,neuralnetworks,backpropagation"
}

@online{CNNResnet,
    author = "Jeff Prosise",
    title = "Facial Recognition with CNNs",
    url  = "https://www.atmosera.com/blog/facial-recognition-with-cnns/",
    addendum = "(accessed: 14.04.2024)",
    keywords = "latex,CNN,Resnet"
}
    </pre>
</div>

</div>

## Acknowledgment
We would like to express my sincere gratitude to Anand Mishra, Assitant Professor, for this course project .
