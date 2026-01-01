# MLFeatureValue

**Class**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

A generic wrapper around an underlying value and the value’s type.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
class MLFeatureValue
```

## Overview

A Core ML *feature value* wraps an underlying value and bundles it with that value’s type, which is one of the types that [MLFeatureType](mlfeaturetype.md) defines. Apps typically access feature values indirectly by using the methods in the wrapper class Xcode automatically generates for Core ML model files.

If your app accesses an [MLModel](mlmodel.md) directly, it must create and consume [MLFeatureProvider](mlfeatureprovider.md) instances. For each prediction, Core ML accepts a feature provider for its inputs, and generates a separate feature provider for its outputs. The input feature provider contains one `MLFeatureValue` instance per input, and the output feature provider contains one per output. See [MLFeatureDescription](mlfeaturedescription.md) for more information about the model input and output features.

## Topics

### Creating a feature value

- [init(_:)](mlfeaturevalue/init(_:).md)
  Creates a feature value from a sendable feature value.

### Creating numeric feature values

- [init(int64:)](mlfeaturevalue/init(int64:).md)
  Creates a feature value that contains an integer.

- [init(double:)](mlfeaturevalue/init(double:).md)
  Creates a feature value that contains a double.

### Creating string feature values

- [init(string:)](mlfeaturevalue/init(string:).md)
  Creates a feature value that contains a string.

### Creating multidimensional feature values

- [init(multiArray:)](mlfeaturevalue/init(multiarray:).md)
  Creates a feature value that contains a multidimensional array.

- [init(shapedArray:)](mlfeaturevalue/init(shapedarray:).md)
  Creates a feature value that contains a shaped array.

### Creating collection feature values

- [init(dictionary:)](mlfeaturevalue/init(dictionary:).md)
  Creates a feature value that contains a dictionary of numbers.

- [init(sequence:)](mlfeaturevalue/init(sequence:).md)
  Creates a feature value that contains a sequence.

### Creating image feature values

- [init(pixelBuffer:)](mlfeaturevalue/init(pixelbuffer:).md)
  Creates a feature value that contains an image from a pixel buffer.

- [init(CGImage:pixelsWide:pixelsHigh:pixelFormatType:options:)](mlfeaturevalue/init(cgimage:pixelswide:pixelshigh:pixelformattype:options:).md)
  Creates a feature value that contains an image defined by a core graphics image and its size and pixel format.

- [init(CGImage:orientation:pixelsWide:pixelsHigh:pixelFormatType:options:)](mlfeaturevalue/init(cgimage:orientation:pixelswide:pixelshigh:pixelformattype:options:).md)
  Creates a feature value that contains an image defined by a core graphics image and its orientation, size, and pixel format.

- [init(CGImage:constraint:options:)](mlfeaturevalue/init(cgimage:constraint:options:).md)
  Creates a feature value that contains an image defined by a core graphics image and a constraint.

- [init(CGImage:orientation:constraint:options:)](mlfeaturevalue/init(cgimage:orientation:constraint:options:).md)
  Creates a feature value that contains an image defined by a core graphics image, an orientation, and a constraint.

- [init(imageAtURL:pixelsWide:pixelsHigh:pixelFormatType:options:)](mlfeaturevalue/init(imageaturl:pixelswide:pixelshigh:pixelformattype:options:).md)
  Creates a feature value that contains an image defined by an image URL and the image’s size and pixel format.

- [init(imageAtURL:orientation:pixelsWide:pixelsHigh:pixelFormatType:options:)](mlfeaturevalue/init(imageaturl:orientation:pixelswide:pixelshigh:pixelformattype:options:).md)
  Creates a feature value that contains an image defined by an image URL and the image’s orientation, size, and pixel format.

- [init(imageAtURL:constraint:options:)](mlfeaturevalue/init(imageaturl:constraint:options:).md)
  Creates a feature value that contains an image defined by an image URL and a constraint.

- [init(imageAtURL:orientation:constraint:options:)](mlfeaturevalue/init(imageaturl:orientation:constraint:options:).md)
  Creates a feature value that contains an image defined by an image URL, an orientation, and a constraint.

- [MLImageConstraint](mlimageconstraint.md)
  The width, height, and pixel format constraints of an image feature.

- [MLFeatureValue.ImageOption](mlfeaturevalue/imageoption.md)
  The initializer options you use to crop and scale an image when creating an image feature value.

### Creating undefined feature values

- [init(undefined:)](mlfeaturevalue/init(undefined:).md)
  Creates a feature value with a type that represents an undefined or missing value.

### Accessing the feature’s type

- [type](mlfeaturevalue/type.md)
  The type of the feature value.

### Accessing the feature’s value

- [isUndefined](mlfeaturevalue/isundefined.md)
  A Boolean value that indicates whether the feature value is undefined or missing.

- [int64Value](mlfeaturevalue/int64value.md)
  The underlying integer of the feature value.

- [doubleValue](mlfeaturevalue/doublevalue.md)
  The underlying double of the feature value.

- [stringValue](mlfeaturevalue/stringvalue.md)
  The underlying string of the feature value.

- [imageBufferValue](mlfeaturevalue/imagebuffervalue.md)
  The underlying image of the feature value as a pixel buffer.

- [shapedArrayValue(of:)](mlfeaturevalue/shapedarrayvalue(of:).md)
  Returns the underlying shaped array of the feature value.

- [multiArrayValue](mlfeaturevalue/multiarrayvalue.md)
  The underlying multiarray of the feature value.

- [sequenceValue](mlfeaturevalue/sequencevalue.md)
  The underlying sequence of the feature value.

- [dictionaryValue](mlfeaturevalue/dictionaryvalue.md)
  The underlying dictionary of the feature value.

### Comparing feature values

- [isEqual(to:)](mlfeaturevalue/isequal(to:).md)
  Returns a Boolean value that indicates whether a feature value is equal to another.

### Supporting types

- [MLFeatureType](mlfeaturetype.md)
  The possible types for feature values, input features, and output features.

- [MLShapedArray](mlshapedarray.md)
  A machine learning collection type that stores scalar values in a multidimensional array.

- [MLShapedArrayProtocol](mlshapedarrayprotocol.md)
  An interface that defines a shaped array type.

- [MLMultiArray](mlmultiarray.md)
  A machine learning collection type that stores numeric values in an array with multiple dimensions.

- [MLSequence](mlsequence.md)
  A machine learning collection type that stores a series of strings or integers.

## See Also

### Model inputs and outputs

- [Making Predictions with a Sequence of Inputs](making-predictions-with-a-sequence-of-inputs.md)
  Integrate a recurrent neural network model to process sequences of inputs.

- [MLSendableFeatureValue](mlsendablefeaturevalue.md)
  A sendable feature value.

- [MLFeatureProvider](mlfeatureprovider.md)
  An interface that represents a collection of values for either a model’s input or its output.

- [MLDictionaryFeatureProvider](mldictionaryfeatureprovider.md)
  A convenience wrapper for the given dictionary of data.

- [MLBatchProvider](mlbatchprovider.md)
  An interface that represents a collection of feature providers.

- [MLArrayBatchProvider](mlarraybatchprovider.md)
  A convenience wrapper for batches of feature providers.

- [MLModelAsset](mlmodelasset.md)
  An abstraction of a compiled Core ML model asset.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
