# init(forModelAtURL:trainingData:completionHandler:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLUpdateTask](../mlupdatetask.md)

---

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
convenience init(forModelAtURL modelURL: URL, trainingData: any MLBatchProvider, completionHandler: @escaping (MLUpdateContext) -> Void) throws
```

## See Also

### Creating an update task

- [init(forModelAt:trainingData:completionHandler:)](init(formodelat:trainingdata:completionhandler:).md)
  Creates a task that updates the model at the URL with the training data, and calls the completion handler when the update completes.

- [init(forModelAt:trainingData:progressHandlers:)](init(formodelat:trainingdata:progresshandlers:).md)
  Creates a task that updates the model at the URL with the training data, and calls the progress handlers during and after the update.

- [init(forModelAt:trainingData:configuration:completionHandler:)](init(formodelat:trainingdata:configuration:completionhandler:).md)
  Creates a task that updates the model at the URL with the training data and configuration, and calls the completion handler when the update completes.

- [init(forModelAt:trainingData:configuration:progressHandlers:)](init(formodelat:trainingdata:configuration:progresshandlers:).md)
  Creates a task that updates the model at the URL with the training data and configuration, and calls the progress handlers during and after the update.

- [init(forModelAtURL:trainingData:progressHandlers:)](init(formodelaturl:trainingdata:progresshandlers:).md)

- [init(forModelAtURL:trainingData:configuration:completionHandler:)](init(formodelaturl:trainingdata:configuration:completionhandler:).md)

- [init(forModelAtURL:trainingData:configuration:progressHandlers:)](init(formodelaturl:trainingdata:configuration:progresshandlers:).md)

- [MLBatchProvider](../mlbatchprovider.md)
  An interface that represents a collection of feature providers.

- [MLModelConfiguration](../mlmodelconfiguration.md)
  The settings for creating or updating a machine learning model.

- [MLUpdateContext](../mlupdatecontext.md)
  The context an update task provides to your app’s completion and update progress handlers.

- [MLUpdateProgressHandlers](../mlupdateprogresshandlers.md)
  A collection of closures an update task uses to notify your app of its progress.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
