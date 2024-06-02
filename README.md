# Linear Transformations
## Description
- **The goal:** to generate, manipulate, and visualize 2D and 3D objects represented as arrays of coordinates.
- **Functionality:** plotting, scaling by a factor, rotating around, projecting onto, mirroring, and shearing along a specified axis.
- **Objects:** McDonald's logo, Nike 'Swoosh' logo, pyramid, penguin image.
- **Tools:** Python, Numpy, Matplotlib, OpenCV.

## Theoretical intro
_**A linear transformation**_, aka linear operator, is a function that maps vectors from one vector space to another while preserving the underlying linear structure alongside additivity and scalar multiplication properties. It finds its **_application_** in distinct tasks, mostly related to computer graphics: image compression, denoising, and 3D rendering showcasing graphics vector nature ([R2](https://github.com/kzholtikova/linear-transformations/releases/tag/image-transformations-and-verification)). However, these are not the only, as it's widely used in machine learning and network flow problems.<br>
**Matrix of a linear transformation** is a unique matrix that holds 𝑇(𝑥⃗)=𝐴𝑥⃗ property for every 𝑥⃗ in the transformation domain. This can be **interpreted as** applying the transformation to a vector produces the same result as multiplying by the matrix of a map. What's interesting here each linear operator has only one corresponding standard matrix consisting of transformed vectors of the standard basis of the domain.<br>

For instance, **rotation matrix** is a square matrix. Its forms for 3-dimensional space alters according to the pivot axis: ![](https://github.com/kzholtikova/linear-transformations/assets/145042018/f9d42804-9c72-4eee-9178-1b2ca8a8546c)

For 2D it's always the same 2*2 matrix, where θ reflects the rotation angle.<br>

I must emphasize that the result of a sequence of transformations depends on their **order** unless they're of one kind or affect the same matrix elements ([R1](https://github.com/kzholtikova/linear-transformations/releases/tag/linear-transformation-implementation)).<br>

The inverse linear operator comes in handy, when **reverting** the transformation is requested. Specifically, mirroring requires repeating the same transformation, whereas the rotation effect can be cancelled by rotating by -θ. Not every operator **has its inverse** though: projection cannot be undone.<br>

The absolute value of a determinant of a map matrix relates to the scale factor obtained by the corresponding transformation. It reflects the area enlargement for the 2D plane and the volume for the 3D space. Inherently, the factor of 1 implies no changes, while 0 reduces the figure to a single dot. Hence, if the absolute value is greater than 1, the scale increases, and vice versa.

## Outcomes
Check all releases with outcomes proofs here:
- [Linear transformation implementation (R1)](https://github.com/kzholtikova/linear-transformations/releases/tag/linear-transformation-implementation)
- [Image transformations and Methods verification (R2)](https://github.com/kzholtikova/linear-transformations/releases/tag/image-transformations-and-verification)
