# MLModelMetadataKey

**Structure**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

The set of keys the model uses to store values in its metadata dictionary.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
struct MLModelMetadataKey
```

## Topics

### Metadata keys

- [author](mlmodelmetadatakey/author.md)
  Key for the author of the model.

- [description](mlmodelmetadatakey/description.md)
  Key for the overall description of the model.

- [license](mlmodelmetadatakey/license.md)
  Key for the license of the model.

- [versionString](mlmodelmetadatakey/versionstring.md)
  Key for the version of the model.

- [creatorDefinedKey](mlmodelmetadatakey/creatordefinedkey.md)
  Key for the model creator’s custom metadata.

### Creating metadata

- [init(rawValue:)](mlmodelmetadatakey/init(rawvalue:).md)

## See Also

### Accessing metadata

- [classLabels](mlmodeldescription/classlabels.md)
  An array of labels, which can be either strings or a numbers, for classifier models.

- [metadata](mlmodeldescription/metadata.md)
  A dictionary of the model’s creation information, such as its description, author, version, and license.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
