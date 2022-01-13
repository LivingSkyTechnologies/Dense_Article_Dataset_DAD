# Dense Article Dataset (DAD)

## About

We aim to construct a comprehensive Dense Article Dataset (DAD) that:

(1) covers research articles from multiple disciplines, and 
(2) captures the detailed elements in a research article in its orginal publication format. The constructed dataset should facilitate the training of robust deep learning document structure extraction models.

We collect research articles from 14 different journals published by five major journal publishers: Elsevier, Springer, SAGE publisher, Wiley, and IEEE.Noted that the research articles collected from the five major publishers are open access papers.

We adopt a coding scheme proposed in Bateman et al. (2002) to annotate the collected research articles. Specifically, we segment an research article into three main sections: front matters, body matters, and back matters (constantin et al., 2013). The individual sections are further subdivided into various components, which form the basic coding schema used in our annotation. We utilize the Microsoft annotation tool, VOTT, to annotate our collected dataset. The annotation of each research article is saved as a JSON file in LabelMe format. 

If you use our work, please cite using the following information:
```
﻿@Article{DAD,
author={Markewich, Logan
        and Zhang, Hao
        and Xing, Yubin
        and Lambert-Shirzad, Navid
        and Jiang, Zhexin
        and Lee, Roy Ka-Wei
        and Li, Zhi
        and Ko, Seok-Bum},
title={Segmentation for document layout analysis: not dead yet},
journal={International Journal on Document Analysis and Recognition (IJDAR)},
year={2022},
month={Jan},
day={13},
abstract={Document layout analysis is often the first task in document understanding systems, where a document is broken down into identifiable sections. One of the most common approaches to this task is image segmentation, where each pixel in a document image is classified. However, this task is challenging because as the number of classes increases, small and infrequent objects often get missed. In this paper, we propose a weighted bounding box regression loss methodology to improve accuracy for segmentation of document layouts, while demonstrating our results on our dense article dataset (DAD) and the existing PubLayNet dataset. First, we collect and annotate 43 document object classes across 450 open access research articles, constructing DAD. After benchmarking several segmentation networks, we achieve an F1 score of 96.26{\%} on DAD and 97.11{\%} on PubLayNet with DeeplabV3+, while also showing a bounding box regression method for segmentation results that improves the F1 by +1.99 points on DAD. Finally, we demonstrate the networks trained on DAD can be used as a bootstrapped annotation tool for the existing document layout datasets, decreasing annotation time by 38{\%} with DeeplabV3+.},
issn={1433-2825},
doi={10.1007/s10032-021-00391-3},
url={https://doi.org/10.1007/s10032-021-00391-3}
}
```

## Usage

We strongly recommend refering the the documentation and scripts found in our models repository at https://github.com/LivingSkyTechnologies/Document\_Layout\_Segmentation. However, we also provide an example\_usage.ipynb to get someone quickly acqainted with the dataset.

## Annotation Format

Below is an example of the LabelMe JSON format of each annotation file.

```
{
  "version": "4.2.10",
  "flags": {},
  "imagePath": "jpg_image_name.jpg"
  "imageData": null,
  "imageHeight": 2205,
  "imageWidth": 1654,
  "shapes": [
    {
      "label": "label_name",
      "points": [
        [
          min_x,  # pixel locations as floats
          min_y
        ],
        [
          max_x,
          max_y
        ]
      ],
      "group_id": 1,  # The integer label in the mask (if given)
      "shape_type": "rectangle",
      "flags": {}
    },
    ...
  ]
}
```

## References

Bateman, J., Deliny, J., & Henschelz, R. (2002). XML and multimodal corpus design: Experiences with multi-layered stand-off annotations in the GeM corpus. LREC’02 Workshop: Towards a Roadmap for Multimodal Language Resources and Evaluation, 7–14.

Constantin, A., Pettifer, S., & Voronkov, A. (2013). PDFX: Fully-automated PDF-to-XML conversion of scientific literature. Proceedings of the 2013 ACM Symposium on Document Engineering - DocEng ’13, 177. https://doi.org/10.1145/2494266.2494271
