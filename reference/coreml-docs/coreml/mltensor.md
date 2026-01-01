# MLTensor

**Structure**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

A multi-dimensional array of numerical or Boolean scalars tailored to ML use cases, containing methods to perform transformations and mathematical operations efficiently using a ML compute device.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
struct MLTensor
```

## Topics

### Creating a tensor

- [init(_:)](mltensor/init(_:).md)
  Creates a one-dimensional tensor from scalars.

- [init(_:alongAxis:)](mltensor/init(_:alongaxis:).md)
  Creates a tensor by stacking the given tensors along the specified axis.

- [init(_:scalarType:)](mltensor/init(_:scalartype:).md)
  Creates a one-dimensional tensor from scalars.

- [init(bytesNoCopy:shape:scalarType:deallocator:)](mltensor/init(bytesnocopy:shape:scalartype:deallocator:).md)
  Creates a tensor with memory content without copying the bytes.

- [init(concatenating:alongAxis:)](mltensor/init(concatenating:alongaxis:).md)
  Concatenates `tensors` along the `axis` dimension.

- [init(linearSpaceFrom:through:count:)](mltensor/init(linearspacefrom:through:count:).md)
  Creates a one-dimensional tensor representing a sequence from a starting value, up to and including an end value, spaced evenly to generate the number of values specified.

- [init(linearSpaceFrom:through:count:scalarType:)](mltensor/init(linearspacefrom:through:count:scalartype:).md)
  Creates a one-dimensional tensor representing a sequence from a starting value, up to and including an end value, spaced evenly to generate the number of values specified.

- [init(ones:scalarType:)](mltensor/init(ones:scalartype:).md)
  Creates a tensor with all scalars set to ones.

- [init(randomNormal:mean:standardDeviation:seed:scalarType:)](mltensor/init(randomnormal:mean:standarddeviation:seed:scalartype:).md)
  Creates a tensor with the specified shape, randomly sampling scalar values from a normal distribution.

- [init(randomUniform:in:seed:scalarType:)](mltensor/init(randomuniform:in:seed:scalartype:).md)
  Creates a tensor with the specified shape, randomly sampling scalar values from a uniform distribution in `bounds`.

- [init(rangeFrom:to:by:)](mltensor/init(rangefrom:to:by:).md)
  Creates a one-dimensional tensor representing a sequence from a starting value to, but not including, an end value, stepping by the specified amount.

- [init(rangeFrom:to:by:scalarType:)](mltensor/init(rangefrom:to:by:scalartype:).md)
  Creates a one-dimensional tensor representing a sequence from a starting value to, but not including, an end value, stepping by the specified amount.

- [init(repeating:shape:)](mltensor/init(repeating:shape:).md)
  Creates a tensor with the specified shape and a single, repeated scalar value.

- [init(repeating:shape:scalarType:)](mltensor/init(repeating:shape:scalartype:).md)
  Creates a tensor with the specified shape and a single, repeated scalar value.

- [init(shape:data:scalarType:)](mltensor/init(shape:data:scalartype:).md)
  Creates a tensor by copying the given block of data.

- [init(shape:scalars:)](mltensor/init(shape:scalars:).md)
  Creates a tensor with the specified shape and contiguous scalars in first-major order.

- [init(shape:scalars:scalarType:)](mltensor/init(shape:scalars:scalartype:).md)
  Creates a tensor with the specified shape and contiguous scalars in row-major order.

- [init(stacking:alongAxis:)](mltensor/init(stacking:alongaxis:).md)
  Stacks the given tensors along the `axis` dimension into a new tensor with rank one higher than the current tensor and each tensor.

- [init(unsafeUninitializedShape:scalarType:initializingWith:)](mltensor/init(unsafeuninitializedshape:scalartype:initializingwith:).md)
  Creates a tensor with the specified shape, then calls the given closure with a buffer covering the tensor’s uninitialized memory.

- [init(zeros:scalarType:)](mltensor/init(zeros:scalartype:).md)
  Creates a tensor with all scalars set to zero.

### Accessing tensor properties

- [isScalar](mltensor/isscalar.md)
  A Boolean value indicating whether the tensor is a scalar (when the `rank` is equal to `0`) or not.

- [rank](mltensor/rank.md)
  The number of dimensions of the tensor.

- [scalarCount](mltensor/scalarcount.md)
  The number of scalar elements in the tensor.

- [scalarType](mltensor/scalartype.md)
  The type of scalars in the tensor.

- [shape](mltensor/shape.md)
  The shape of the tensor.

### Getting the sum

- [sum(alongAxes:keepRank:)](mltensor/sum(alongaxes:keeprank:).md)
  Returns the sum along the specified axes.

- [sum(keepRank:)](mltensor/sum(keeprank:).md)
  Returns the sum along all axes.

### Performing a logical AND operation

- [all(alongAxes:keepRank:)](mltensor/all(alongaxes:keeprank:).md)
  Computes logical AND on elements across the specified axes of a tensor where the scalar type of the tensor is expected to be Boolean.

- [all(keepRank:)](mltensor/all(keeprank:).md)
  Computes logical AND on elements across all axes of a tensor where the scalar type of the tensor is expected to be Boolean.

### Performing a logical OR operation

- [any(alongAxes:keepRank:)](mltensor/any(alongaxes:keeprank:).md)
  Computes logical OR on elements across the specified axes of a tensor where the scalar type of the tensor is expected to be Boolean.

- [any(keepRank:)](mltensor/any(keeprank:).md)
  Computes logical OR on elements across all dimensions of a tensor where the scalar type of the tensor is expected to be Boolean.

### Accessing the indicies

- [argmax()](mltensor/argmax().md)
  Returns the index of the maximum value of the flattened scalars.

- [argmax(alongAxis:keepRank:)](mltensor/argmax(alongaxis:keeprank:).md)
  Returns the indices of the maximum values along the specified axis.

- [argmin()](mltensor/argmin().md)
  Returns the index of the minimum value of the flattened scalars.

- [argmin(alongAxis:keepRank:)](mltensor/argmin(alongaxis:keeprank:).md)
  Returns the indices of the minimum values along the specified axis.

- [argsort(alongAxis:descendingOrder:)](mltensor/argsort(alongaxis:descendingorder:).md)
  Returns the indices (or arguments) of a tensor that give its sorted order along the specified axis.

### Casting the elements

- [cast(like:)](mltensor/cast(like:).md)
  Casts the elements of the tensor to the scalar type of the given array.

- [cast(to:)](mltensor/cast(to:).md)
  Casts the elements of the tensor to the given scalar type.

### Computing the absolute, ceiling and floor

- [abs()](mltensor/abs().md)
  Computes the absolute of the tensor’s elements.

- [ceil()](mltensor/ceil().md)
  Computes the ceiling of the tensor’s elements.

- [floor()](mltensor/floor().md)
  Computes the floor of the tensor’s elements.

### Performing arithmetic operations

- [*(_:_:)](mltensor/*(_:_:).md)
  Computes element-wise multiplication.

- [*=(_:_:)](mltensor/*=(_:_:).md)
  Computes element-wise multiplication.

- [+(_:_:)](mltensor/+(_:_:).md)
  Computes element-wise addition.

- [+=(_:_:)](mltensor/+=(_:_:).md)
  Computes element-wise addition.

- [-(_:)](mltensor/-(_:).md)
  Returns the negation of the tensor.

- [-(_:_:)](mltensor/-(_:_:).md)
  Computes element-wise subtraction.

- [-=(_:_:)](mltensor/-=(_:_:).md)
  Computes element-wise subtraction.

- [.!(_:)](mltensor/'.!(_:).md)
  Computes logical not on the tensor’s elements.

- [.!=(_:_:)](mltensor/'.!=(_:_:).md)
  Computes element-wise inequality between two tensors.

- [.&(_:_:)](mltensor/'.&(_:_:).md)
  Computes element-wise logical AND where both operands are expected contain Boolean scalar elements.

- [.==(_:_:)](mltensor/'.==(_:_:).md)
  Computes element-wise equality between two tensors.

- [.>(_:_:)](mltensor/'._(_:_:)-3m3ro.md)
  Computes element-wise greater comparison between two tensors.

- [.<(_:_:)](mltensor/'._(_:_:)-6kfoh.md)
  Computes element-wise less comparison between two tensors.

- [.|(_:_:)](mltensor/'._(_:_:)-7z7ks.md)
  Computes element-wise logical OR where both operands are expected contain Boolean scalar elements.

- [.^(_:_:)](mltensor/'._(_:_:)-8il7w.md)
  Computes element-wise logical XOR where both operands are expected contain Boolean scalar elements.

- [.>=(_:_:)](mltensor/'._=(_:_:)-5qa2u.md)
  Computes element-wise greater than or equal to comparison between two tensors.

- [.<=(_:_:)](mltensor/'._=(_:_:)-otif.md)
  Computes element-wise less than or equal to comparison between two tensors.

- [/(_:_:)](mltensor/_(_:_:)-5hhe4.md)
  Computes element-wise division.

- [%(_:_:)](mltensor/_(_:_:)-7cfjs.md)
  Computes element-wise remainder of division.

- [%=(_:_:)](mltensor/_=(_:_:)-3xllm.md)
  Computes element-wise remainder of division.

- [/=(_:_:)](mltensor/_=(_:_:)-53k1k.md)
  Computes element-wise multiplication.

### Applying trigonometric functions

- [cos()](mltensor/cos().md)
  Computes the cosine of the tensor’s elements.

- [cosh()](mltensor/cosh().md)
  Computes the hyperbolic cosine of the tensor’s elements.

- [acos()](mltensor/acos().md)
  Computes the inverse cosine of the tensor’s elements.

- [acosh()](mltensor/acosh().md)
  Computes the inverse hyperbolic cosine of the tensor’s elements.

- [sin()](mltensor/sin().md)
  Computes sine of the tensor’s elements.

- [sinh()](mltensor/sinh().md)
  Computes hyperbolic sine of the tensor’s elements.

- [asin()](mltensor/asin().md)
  Computes the inverse sine of the tensor’s elements.

- [asinh()](mltensor/asinh().md)
  Computes the inverse hyperbolic sine of the tensor’s elements.

- [tan()](mltensor/tan().md)
  Computes tangent of the tensor’s elements.

- [tanh()](mltensor/tanh().md)
  Computes hyperbolic tangent of the tensor’s elements.

- [atan()](mltensor/atan().md)
  Computes the inverse tangent of the tensor’s elements.

- [atanh()](mltensor/atanh().md)
  Computes the inverse hyperbolic tangent of the tensor’s elements.

### Accessing the minimum, maximum and mean

- [min(alongAxes:keepRank:)](mltensor/min(alongaxes:keeprank:).md)
  Returns the minimum values along the specified axes.

- [min(keepRank:)](mltensor/min(keeprank:).md)
  Returns the minimum value in the array.

- [max(alongAxes:keepRank:)](mltensor/max(alongaxes:keeprank:).md)
  Returns the maximum values along the specified axes.

- [max(keepRank:)](mltensor/max(keeprank:).md)
  Returns the maximum value in the array.

- [mean(alongAxes:keepRank:)](mltensor/mean(alongaxes:keeprank:).md)
  Returns the mean along the specified axes.

- [mean(keepRank:)](mltensor/mean(keeprank:).md)
  Returns the mean along all axes.

### Splitting the tensor

- [split(count:alongAxis:)](mltensor/split(count:alongaxis:).md)
  Splits a tensor into multiple tensors. The tensor is split along dimension `axis` into `count` smaller tensors.

- [split(sizes:alongAxis:)](mltensor/split(sizes:alongaxis:).md)
  Splits a tensor into multiple tensors. The tensor is split  into `sizes.shape[0]` parts.

### Resizing the tensor

- [resized(to:method:)](mltensor/resized(to:method:).md)
  Resize the tensor’s spatial dimensions to size using the specified method.

- [MLTensor.ResizeMethod](mltensor/resizemethod.md)
  A resize algorithm.

### Padding the tensor

- [padded(forSizes:mode:)](mltensor/padded(forsizes:mode:).md)
  Returns a padded tensor according to the specified padding sizes and mode.

- [padded(forSizes:with:)](mltensor/padded(forsizes:with:).md)
  Returns a tensor padded with the given constant according to the specified padding sizes.

- [MLTensor.PaddingMode](mltensor/paddingmode.md)
  A mode that dictates how a tensor is padded.

### Replacing the tensor values

- [replacing(atIndices:with:alongAxis:)](mltensor/replacing(atindices:with:alongaxis:).md)
  Replaces slices along the specified indices with the given replacement values.

- [replacing(with:atIndices:alongAxis:)](mltensor/replacing(with:atindices:alongaxis:).md)
  Replaces slices along the specified indices with the given replacement values.

- [replacing(with:where:)](mltensor/replacing(with:where:).md)
  Returns a new tensor replacing values from `other` with the corresponding element in `self` where the associated element in `mask` is `true`.

### Gathering slices

- [gathering(atIndices:)](mltensor/gathering(atindices:).md)
  Returns a tensor by gathering slices at the specified indices.

- [gathering(atIndices:alongAxis:)](mltensor/gathering(atindices:alongaxis:).md)
  Returns a tensor by gathering slices along the given axis at the specified indices.

### Transposing the tensor

- [transposed()](mltensor/transposed().md)
  Permutes the tensor with dimensions permuted in reverse order.

- [transposed(permutation:)](mltensor/transposed(permutation:).md)
  Permutes the dimensions of the tensor in the specified order.

### Unpacking the tensor

- [unstacked(alongAxis:)](mltensor/unstacked(alongaxis:).md)
  Unpacks the given dimension of a rank-`R` tensor into multiple rank-`(R-1)` tensors.

### Getting the shaped representation of the tensor

- [shapedArray(of:)](mltensor/shapedarray(of:).md)
  Returns a materialized representation of the tensor.

### Removing dimensions from the shape of the tensor

- [squeezingShape()](mltensor/squeezingshape().md)
  Removes all dimensions of size 1 from the shape of the tensor.

- [squeezingShape(at:)](mltensor/squeezingshape(at:).md)
  Removes the specified dimensions of size 1 from the shape of the tensor.

### Accessing the product along an axes

- [product(alongAxes:keepRank:)](mltensor/product(alongaxes:keeprank:).md)
  Returns the product along the specified axes.

- [product(keepRank:)](mltensor/product(keeprank:).md)
  Returns the product along all axes.

### Getting the largest values

- [topK(_:)](mltensor/topk(_:).md)
  Returns the *k* largest values along the last axis of the tensor.

### Clamping and concatenating

- [clamped(to:)](mltensor/clamped(to:).md)
  Clamps all elements to the given lower and upper bounds, inclusively.

- [concatenated(with:alongAxis:)](mltensor/concatenated(with:alongaxis:).md)
  Returns a concatenated tensor along the specified axis.

### Computing the cumulative value

- [cumulativeProduct(alongAxis:)](mltensor/cumulativeproduct(alongaxis:).md)
  Computes the cumulative product along the specified axis.

- [cumulativeSum(alongAxis:)](mltensor/cumulativesum(alongaxis:).md)
  Computes the cumulative sum along the specified axis.

### Computing the exponent, pow and square root

- [exp()](mltensor/exp().md)
  Computes the natural exponent of the tensor’s elements.

- [exp2()](mltensor/exp2().md)
  Computes the exponent with base two of the tensor’s elements.

- [pow(_:)](mltensor/pow(_:).md)
  Computes element-wise power of each element with `exponent`.

- [rsqrt()](mltensor/rsqrt().md)
  Computes reverse square root of the tensor’s elements.

- [squared()](mltensor/squared().md)
  Computes square of the tensor’s elements.

- [squareRoot()](mltensor/squareroot().md)
  Computes square root of the tensor’s elements.

- [log()](mltensor/log().md)
  Computes the natural logarithm of the tensor’s elements.

- [round()](mltensor/round().md)
  Rounds the tensor’s elements.

- [matmul(_:)](mltensor/matmul(_:).md)
  Multiplies two tensors together using matrix multiplication.

### Accessing the extended tensor, sign and reciprocal

- [expandingShape(at:)](mltensor/expandingshape(at:).md)
  Returns a shape-expanded tensor with a dimension of 1 inserted at the specified shape indices.

- [bandPart(lowerBandCount:upperBandCount:)](mltensor/bandpart(lowerbandcount:upperbandcount:).md)
  Returns a new tensor with the same shape where everything outside a central band in each innermost matrix is set to zero.

- [tiled(multiples:)](mltensor/tiled(multiples:).md)
  Returns a tensor by replicating its elements multiple times.

- [sign()](mltensor/sign().md)
  Returns the sign of the tensor’s elements.

- [reciprocal()](mltensor/reciprocal().md)
  Computes the reciprocal of the tensor’s elements.

### Reshaping the tensor

- [flattened()](mltensor/flattened().md)
  Reshape to a one-dimensional tensor.

- [reshaped(to:)](mltensor/reshaped(to:).md)
  Reshape to the specified shape.

### Computing the softmax

- [softmax(alongAxis:)](mltensor/softmax(alongaxis:).md)
  Computes the softmax of the specified tensor along the specified axis.

### Reversing the tensor

- [reversed(alongAxes:)](mltensor/reversed(alongaxes:).md)
  Returns a new tensor with the specified dimensions reversed.

### Accessing a multiarray’s elements

- [subscript(_:)](mltensor/subscript(_:).md)

- [subscript(_:_:)](mltensor/subscript(_:_:).md)

- [subscript(_:_:_:)](mltensor/subscript(_:_:_:).md)

- [subscript(_:_:_:_:)](mltensor/subscript(_:_:_:_:).md)

- [subscript(_:_:_:_:_:)](mltensor/subscript(_:_:_:_:_:).md)

### Default Implementations

- [CustomReflectable Implementations](mltensor/customreflectable-implementations.md)

## See Also

### Model tensor

- [MLTensorScalar](mltensorscalar.md)
  A type that represents the tensor scalar types supported by the framework. Don’t use this type directly.

- [MLTensorRangeExpression](mltensorrangeexpression.md)
  A type that can be used to slice a dimension of a tensor. Don’t use this type directly.

- [pointwiseMin(_:_:)](pointwisemin(_:_:).md)
  Computes the element-wise minimum of two tensors.

- [pointwiseMax(_:_:)](pointwisemax(_:_:).md)
  Computes the element-wise minimum between two tensors.

- [withMLTensorComputePolicy(_:_:)](withmltensorcomputepolicy(_:_:).md)
  Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
