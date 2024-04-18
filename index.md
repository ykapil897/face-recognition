<link rel="stylesheet" href="style.css">
<script src="script.js" defer></script>

<h1 align="center">
  Face-Recognition of Famous Personalities
</h1>

<h4 align="center">
  Kapil Yadav, Vivek Sapkal, Heramb Gavankar, Raj Patel, Arsewad Bhagwan, Suhani, Jatin
</h4>

<h4 align="center">
  <a href="#">Code</a> | <a href="#">Dataset</a> | <a href="#">Demo Code</a> | <a href="#">Slides</a> | <a href="https://www.youtube.com/embed/s4F7qeVw5mY">Short Talk</a>
</h4>

<div class="slideshow-container">
  <div class="mySlides fade">
    <img src="images/ACAC.jpg" style="width:100%">
  </div>

  <div class="mySlides fade">
    <img src="images/ACAC.jpg" style="width:100%">
  </div>

  <!-- Add more images as needed -->
</div>

<!-- Dots/bullets -->
<div style="text-align:center; margin-top:20px;">
  <span class="dot"></span>
  <span class="dot"></span>
  <!-- Add more dots as needed -->
</div>


## Abstract
Non-native speakers with limited vocabulary often struggle to name specific objects despite being able to visualize them clearly, e.g., people outside Australia searching for ‘numbats.’ Further, users may want to search for such elusive objects with difficult-to-sketch interactions, e.g., “numbat digging in the ground.” In such common but complex situations, users desire a search interface that accepts composite multimodal queries comprising hand-drawn sketches of “difficult-to-name but easy-to-draw” objects along with text describing “difficult-to-sketch but easy-to-verbalize” object’s attributes or interaction with the scene. This novel problem statement is distinctly different from the previously well-researched TBIR (text-based image retrieval) and SBIR (sketch-based image retrieval) problems. To study this under-explored task, we curate a dataset, CSTBIR (Composite Sketch+Text Based Image Retrieval), consisting of ∼2M queries and 108K natural scene images. Further, as a solution to this problem, we propose a pretrained multimodal transformer-based baseline, STNET (Sketch+Text Network), that uses a hand-drawn sketch to localize relevant objects in the natural scene image, and encodes the text and image to perform image retrieval. In addition to contrastive learning, we propose multiple train- ing objectives that improve the performance of our model. Extensive experiments show that our proposed method outperforms several state-of-the-art retrieval methods for text-only, sketch-only, as well as composite query modalities

## Classification Problem
<p align="center">
  <img src="images/ignus.jpg" alt="My Image" width="50%" height="50%">
</p>

<p align="center">
Composite Sketch+Text Based Image Retrieval: A user wants to search “Numbat digging in the ground” but does not know the word “numbat”, and the interaction “digging in the ground” is not easy to sketch. Thus, the user may use a hand-drawn sketch of "numbat" along with the text "digging in the ground" to retrieve the desired images.
</p>

## Short Talk
<p>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/s4F7qeVw5mY" frameborder="0" allowfullscreen></iframe>
</p>

## BibTex
<div style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
  <pre>
    @InProceedings{cstbir2024aaai,
      author = {Gatti, Prajwal and Parikh, Kshitij Gopal and Paul, Dhriti Prasanna and Gupta, Manish and Mishra, Anand},
      title = {Composite Sketch+Text Queries for Retrieving Objects with Elusive Names and Complex Interactions},
      booktitle = {AAAI},
      year = {2024},
    }
  </pre>
</div>


## Contributors

<div style="display: flex; justify-content: space-between;">

  <div style="display: flex; flex-direction: column; align-items: center; width: 150px; margin-right: 20px;">
    <img src="images/ACAC.jpg" alt="Kapil Yadav" style="width: 150px; height: 150px; object-fit: cover; border-radius: 50%;">
    <p align="center">Kapil Yadav</p>
    <div style="display: flex;">
      <a href="#"><img src="images/linkedin_logo.png" alt="LinkedIn" style="width: 20px; height: 20px; margin-right: 10px;"></a>
      <a href="#"><img src="images/instagram_logo.png" alt="Instagram" style="width: 20px; height: 20px;"></a>
    </div>
  </div>

  <div style="display: flex; flex-direction: column; align-items: center; width: 150px; margin-right: 20px;">
    <img src="images/ACAC.jpg" alt="Vivek Sapkal" style="width: 150px; height: 150px; object-fit: cover; border-radius: 50%;">
    <p align="center">Vivek Sapkal</p>
    <div style="display: flex;">
      <a href="#"><img src="images/linkedin_logo.png" alt="LinkedIn" style="width: 20px; height: 20px; margin-right: 10px;"></a>
      <a href="#"><img src="images/instagram_logo.png" alt="Instagram" style="width: 20px; height: 20px;"></a>
    </div>
  </div>

  <div style="display: flex; flex-direction: column; align-items: center; width: 150px; margin-right: 20px;">
    <img src="images/ACAC.jpg" alt="Vivek Sapkal" style="width: 150px; height: 150px; object-fit: cover; border-radius: 50%;">
    <p align="center">Heramb Gavankar</p>
    <div style="display: flex;">
      <a href="#"><img src="images/linkedin_logo.png" alt="LinkedIn" style="width: 20px; height: 20px; margin-right: 10px;"></a>
      <a href="#"><img src="images/instagram_logo.png" alt="Instagram" style="width: 20px; height: 20px;"></a>
    </div>
  </div>

  <div style="display: flex; flex-direction: column; align-items: center; width: 150px; margin-right: 20px;">
    <img src="images/ACAC.jpg" alt="Vivek Sapkal" style="width: 150px; height: 150px; object-fit: cover; border-radius: 50%;">
    <p align="center">Raj Patel</p>
    <div style="display: flex;">
      <a href="#"><img src="images/linkedin_logo.png" alt="LinkedIn" style="width: 20px; height: 20px; margin-right: 10px;"></a>
      <a href="#"><img src="images/instagram_logo.png" alt="Instagram" style="width: 20px; height: 20px;"></a>
    </div>
  </div>

  <div style="display: flex; flex-direction: column; align-items: center; width: 150px; margin-right: 20px;">
    <img src="images/ACAC.jpg" alt="Vivek Sapkal" style="width: 150px; height: 150px; object-fit: cover; border-radius: 50%;">
    <p align="center">Arsewad Bhagwan</p>
    <div style="display: flex;">
      <a href="#"><img src="images/linkedin_logo.png" alt="LinkedIn" style="width: 20px; height: 20px; margin-right: 10px;"></a>
      <a href="#"><img src="images/instagram_logo.png" alt="Instagram" style="width: 20px; height: 20px;"></a>
    </div>
  </div>

  <div style="display: flex; flex-direction: column; align-items: center; width: 150px; margin-right: 20px;">
    <img src="images/ACAC.jpg" alt="Vivek Sapkal" style="width: 150px; height: 150px; object-fit: cover; border-radius: 50%;">
    <p align="center">Suhani</p>
    <div style="display: flex;">
      <a href="#"><img src="images/linkedin_logo.png" alt="LinkedIn" style="width: 20px; height: 20px; margin-right: 10px;"></a>
      <a href="#"><img src="images/instagram_logo.png" alt="Instagram" style="width: 20px; height: 20px;"></a>
    </div>
  </div>

  <div style="display: flex; flex-direction: column; align-items: center; width: 150px; margin-right: 20px;">
    <img src="images/ACAC.jpg" alt="Vivek Sapkal" style="width: 150px; height: 150px; object-fit: cover; border-radius: 50%;">
    <p align="center">Jatin</p>
    <div style="display: flex;">
      <a href="#"><img src="images/linkedin_logo.png" alt="LinkedIn" style="width: 20px; height: 20px; margin-right: 10px;"></a>
      <a href="#"><img src="images/instagram_logo.png" alt="Instagram" style="width: 20px; height: 20px;"></a>
    </div>
  </div>
</div>

## Acknowledgment
This work is supported by the Startup Research Grant from the Science and Engineering Research Board (SERB), Department of Science and Technology, Government of India (Grant No: SRG/2021/001948).

## Contact
For questions, please contact Prajwal Gatti or raise an issue on GitHub.

<p align="center">
  Copyright © IIT Jodhpur
</p>
