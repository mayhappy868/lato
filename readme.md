# Rebuttal to Reviewer #jbkB

We sincerely thank you for your time and insightful feedback. We appreciate your recognition of our work's **intuitive representation** and its advantages in **efficiency**. 

To address your concerns regarding topology-aware metrics, comparisons against implicit baselines, vertex pair sampling versus full pairwise supervision, and failure cases, we have conducted additional experiments and analyses detailed below.

---

## W1, W4 & Q2: Topology-Aware Metrics Besides CD/HD/NC Values

We appreciate the suggestion to include topology-aware metrics, which further justify our central claim. The quantitative evaluation of topology quality remains an open challenge in the field, and most SOTA methods (including MeshAnything and DeepMesh) rely on user study questionnaires to gather human subjective evaluations. 

Currently, the only works that provide quantitative metrics are MeshRFT and QuadGPT. MeshRFT defines a metric called the **Topology Score**, which converts the original triangular mesh into a quadrilateral mesh and calculates the proportion of uniform, smoothly connected squares. We conducted both a user study and a Topology Score comparison against implicit and auto-regressive baselines, evaluating 200 data-artist meshes and 200 dense meshes.

### Table 1: Comparison of Topology Scores
| Paradigm | Methods | Topology Score ↑ |
| :--- | :---: | :---: |
| **Implicit** | TRELLIS | 0.5264 |
| | Hunyuan3D | 0.2946 |
| | Tripo3D | 0.5146 |
| | CLAY | 0.5100 |
| **Auto-regressive** | DeepMesh | 0.5500 |
| | FastMesh | 0.5470 |
| | BPT | 0.5415 |
| | Mesh Silksong | 0.5223 |
| **T-Voxel Flow Matching** | **Ours** | **0.5551** |

Furthermore, we refined our user study questionnaire, asking participants to select the generated mesh demonstrating both the cleanest topology and the best overall geometry (a screenshot of the questionnaire is provided in `[Insert Link/Image Reference here]`).

### Table 2: User Study Results
| Paradigm | Methods | User Preference Ratio ↑ |
| :--- | :---: | :---: |
| **Implicit** | Hunyuan3D | 0.0486 |
| | Tripo3D | 0.1284 |
| | CLAY | 0.0311 |
| **Auto-regressive** | DeepMesh | 0.0350 |
| | FastMesh | 0.0447 |
| | BPT | 0.1751 |
| | Mesh Silksong | 0.0506 |
| **T-Voxel Flow Matching** | **Ours** | **0.4864** |

---

## W2, W4 & Q1: Quantitative Comparison Against Strong Implicit Baselines

Thank you for this suggestion. As shown in Table 1 above, our LATO model already outperforms strong implicit baselines (including TRELLIS, Hunyuan3D, Tripo3D, and CLAY) in terms of topology-aware metrics. 

To further validate our approach, we provide comparisons on FID and KID values against these baselines. It is important to note that Hunyuan3D, Tripo3D, and CLAY are commercial models that significantly exceed LATO in both parameter count and training data scale. We list these specifications below to provide context for this computationally asymmetric comparison:

### Table 3: Resource & Scale Comparison
| | TRELLIS | Hunyuan3D *(Commercial)* | Tripo3D *(Commercial)* | CLAY *(Commercial)* | **Our LATO** |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Params** | 2B | UNKNOWN | UNKNOWN | 1.5B | **180M** |
| **GPU Time** | 64x A100 (400K steps) | UNKNOWN | 64x A100 (UNKNOWN) | 255x A800 (15 days) | **8x H100 (7 days)** |
| **Training Data**| 500K | UNKNOWN | UNKNOWN | 527K | **400K** |

We computed the FID and KID on 200 meshes from the Objaverse dataset:

### Table 4: Comparison of FID and KID Values
| Methods | FID ↓ | KID (x10³) ↓ |
| :--- | :---: | :---: |
| Tripo3D | 75.85 | 3.126 |
| Hunyuan3D | 76.66 | 3.449 |
| CLAY | 70.91 | 3.016 |
| TRELLIS | 76.78 | 4.157 |
| **Our LATO** | **78.53** | **4.224** |

While LATO's FID/KID values are slightly inferior to those of commercial implicit baselines due to the massive difference in model capacity, the performance remains highly competitive and comparable `[Insert reference to visual results showing this comparison]`.

---

## W3: Resolution Bottleneck

Hunyuan3D, Tripo3D, and CLAY are large-scale commercial models with approximately 10x the parameter count of ours, trained on vast datasets (often >500K assets, including proprietary collections). In contrast, working within academic resource constraints, we scoped our model to 189M parameters and utilized the public Objaverse dataset, where ~80% of our training data contains fewer than 6K triangles. 

We respectfully clarify that our primary objective in `[Insert Figure Reference]` is not to compete purely on geometry resolution with massive commercial models, but rather to demonstrate superior **topology generation capabilities** `[Insert Reference to Topology Figures]`.

Even with a constrained model size and training budget, the experimental results in `[Insert Section/Figure Reference]` and Tables 1 and 2 sufficiently demonstrate that our novel topology-preserving sparse voxel latent representation is highly effective at `[Insert specific achievement, e.g., maintaining sharp feature edges]`. In future work, we plan to scale the model size, curate a dataset of higher-complexity meshes, and incorporate image guidance to generate more refined and detailed geometries.

---

## W4: Quantified Topology and Geometry Quality

The quantified topology and geometry quality comparisons are fully detailed in Tables `[Insert Table Numbers]` and `[Insert Table Numbers]`.

---

## L1: Vertex Pair Sampling Ratio vs. Quality

Thank you for the suggestion to justify our choice of the vertex pair sampling ratio. We selected 5 pairs based on the ablation experiments shown below. The table demonstrates the decoded geometry quality with respect to the sampling ratio (using Chamfer Distance, Hausdorff Distance, and Normal Consistency):

### Table 5: Geometry Quality w.r.t. Sampling Ratio
| Total Sample Points (Nn + Nr) | CD (L2) ↓ | CD (L1) ↓ | HD ↓ | \|NC\| ↑ |
| :--- | :---: | :---: | :---: | :---: |
| 24 (16+8) | 0.0548 | 0.0773 | 0.1243 | 0.7715 |
| 48 (32+16) | 0.0502 | 0.0712 | 0.1115 | 0.7902 |
| 96 (64+32) | 0.0437 | 0.0617 | 0.0940 | 0.8337 |
| 192 (128+64) | **0.0402** | **0.0570** | **0.0786** | **0.8425** |
| 384 (256+128) | OOM | OOM | OOM | OOM |

*(Note: Increasing the sampling points beyond 192 results in Out-Of-Memory (OOM) errors during our standard training setup, making 192 the optimal boundary for quality and hardware efficiency).*
