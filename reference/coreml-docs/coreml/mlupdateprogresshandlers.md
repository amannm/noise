# MLUpdateProgressHandlers

**Class**

**Framework:** Core ML

**Availability:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+, watchOS 6.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

A collection of closures an update task uses to notify your app of its progress.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
class MLUpdateProgressHandlers
```

## Topics

### Creating progress handlers

- [init(forEvents:progressHandler:completionHandler:)](mlupdateprogresshandlers/init(forevents:progresshandler:completionhandler:).md)
  Creates the collection of closures an update task uses to notify your app of its progress.

- [MLUpdateProgressEvent](mlupdateprogressevent.md)
  A type of event during a model update task.

- [MLUpdateContext](mlupdatecontext.md)
  The context an update task provides to your app’s completion and update progress handlers.

## See Also

### Creating an update task

- [init(forModelAt:trainingData:completionHandler:)](mlupdatetask/init(formodelat:trainingdata:completionhandler:).md)
  Creates a task that updates the model at the URL with the training data, and calls the completion handler when the update completes.

- [init(forModelAt:trainingData:progressHandlers:)](mlupdatetask/init(formodelat:trainingdata:progresshandlers:).md)
  Creates a task that updates the model at the URL with the training data, and calls the progress handlers during and after the update.

- [init(forModelAt:trainingData:configuration:completionHandler:)](mlupdatetask/init(formodelat:trainingdata:configuration:completionhandler:).md)
  Creates a task that updates the model at the URL with the training data and configuration, and calls the completion handler when the update completes.

- [init(forModelAt:trainingData:configuration:progressHandlers:)](mlupdatetask/init(formodelat:trainingdata:configuration:progresshandlers:).md)
  Creates a task that updates the model at the URL with the training data and configuration, and calls the progress handlers during and after the update.

- [init(forModelAtURL:trainingData:completionHandler:)](mlupdatetask/init(formodelaturl:trainingdata:completionhandler:).md)

- [init(forModelAtURL:trainingData:progressHandlers:)](mlupdatetask/init(formodelaturl:trainingdata:progresshandlers:).md)

- [init(forModelAtURL:trainingData:configuration:completionHandler:)](mlupdatetask/init(formodelaturl:trainingdata:configuration:completionhandler:).md)

- [init(forModelAtURL:trainingData:configuration:progressHandlers:)](mlupdatetask/init(formodelaturl:trainingdata:configuration:progresshandlers:).md)

- [MLBatchProvider](mlbatchprovider.md)
  An interface that represents a collection of feature providers.

- [MLModelConfiguration](mlmodelconfiguration.md)
  The settings for creating or updating a machine learning model.

- [MLUpdateContext](mlupdatecontext.md)
  The context an update task provides to your app’s completion and update progress handlers.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
