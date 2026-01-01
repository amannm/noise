# init(forModelAt:trainingData:configuration:completionHandler:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+, watchOS 6.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLUpdateTask](../mlupdatetask.md)

---

Creates a task that updates the model at the URL with the training data and configuration, and calls the completion handler when the update completes.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
convenience init(forModelAt modelURL: URL, trainingData: any MLBatchProvider, configuration: MLModelConfiguration?, completionHandler: @escaping (MLUpdateContext) -> Void) throws
```

### Parameters

- **`modelURL`**
  The location in the file system of a model file (*ModelName*`.mlmodelc`).

- **`trainingData`**
  The update data for the model, contained in a batch provider.

- **`configuration`**
  The model settings for an updated model object.

- **`completionHandler`**
  The closure the task calls when it finishes.

## See Also

### Creating an update task

- [init(forModelAt:trainingData:completionHandler:)](init(formodelat:trainingdata:completionhandler:).md)
  Creates a task that updates the model at the URL with the training data, and calls the completion handler when the update completes.

- [init(forModelAt:trainingData:progressHandlers:)](init(formodelat:trainingdata:progresshandlers:).md)
  Creates a task that updates the model at the URL with the training data, and calls the progress handlers during and after the update.

- [init(forModelAt:trainingData:configuration:progressHandlers:)](init(formodelat:trainingdata:configuration:progresshandlers:).md)
  Creates a task that updates the model at the URL with the training data and configuration, and calls the progress handlers during and after the update.

- [init(forModelAtURL:trainingData:completionHandler:)](init(formodelaturl:trainingdata:completionhandler:).md)

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
