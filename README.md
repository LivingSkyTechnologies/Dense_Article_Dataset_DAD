# Dense Article Dataset (DAD)

## About

We aim to construct a comprehensive Dense Article Dataset (DAD) that:

(1) covers research articles from multiple disciplines, and 
(2) captures the detailed elements in a research article in its orginal publication format. The constructed dataset should facilitate the training of robust deep learning document structure extraction models.

We collect research articles from 14 different journals published by five major journal publishers: Elsevier, Springer, SAGE publisher, Wiley, and IEEE.Noted that the research articles collected from the five major publishers are open access papers.

We adopt a coding scheme proposed in Bateman et al. (2002) to annotate the collected research articles. Specifically, we segment an research article into three main sections: front matters, body matters, and back matters (constantin et al., 2013). The individual sections are further subdivided into various components, which form the basic coding schema used in our annotation. We utilize the Microsoft annotation tool, VOTT, to annotate our collected dataset. The annotation of each research article is saved as a JSON file. Each component is labeled in a colored shade that carries detailed information of this component in the JSON file, such as the tag name, the coordinates of the component location, shade color code, etc..  

## Usage

We strongly recommend refering the the documentation and scripts found in our models repository at X. However, we also provide an example_usage.ipynb to get someone quickly acqainted with the dataset.

## References

Bateman, J., Deliny, J., & Henschelz, R. (2002). XML and multimodal corpus design: Experiences with multi-layered stand-off annotations in the GeM corpus. LREC’02 Workshop: Towards a Roadmap for Multimodal Language Resources and Evaluation, 7–14.

Constantin, A., Pettifer, S., & Voronkov, A. (2013). PDFX: Fully-automated PDF-to-XML conversion of scientific literature. Proceedings of the 2013 ACM Symposium on Document Engineering - DocEng ’13, 177. https://doi.org/10.1145/2494266.2494271
