# MLModelStructure

**Enumeration**

**Framework:** Core ML

**Availability:** iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.0+, watchOS 10.4+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

An enum representing the structure of a model.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
enum MLModelStructure
```

## Overview

```None
// Load the model structure.
let modelStructure = await try MLModelStructure.load(contentsOf: modelURL)
switch modelStructure {
case .program(let program):
   // Examine ML Program model.
case .neuralNetwork(let neuralNetwork):
   // Examine Neural network model
case .pipeline(let pipeline)
   // Examine Pipeline model
default:
   // The model type is something else.
}
```

## Topics

### Model structures

- [MLModelStructure.neuralNetwork(_:)](mlmodelstructure-swift.enum/neuralnetwork(_:).md)
  Represents a NeuralNetwork model, the associated value is the structure of the NeuralNetwork.

- [MLModelStructure.NeuralNetwork](mlmodelstructure-swift.enum/neuralnetwork.md)
  A struct representing the structure of a NeuralNetwork model..

- [MLModelStructure.pipeline(_:)](mlmodelstructure-swift.enum/pipeline(_:).md)
  Represents a Pipeline model, the associated value is the structure of the Pipeline.

- [MLModelStructure.Pipeline](mlmodelstructure-swift.enum/pipeline.md)
  A struct representing the structure of a Pipeline model..

- [MLModelStructure.program(_:)](mlmodelstructure-swift.enum/program(_:).md)
  Represents a MLProgram model. the associated value is the structure of the Program.

- [MLModelStructure.Program](mlmodelstructure-swift.enum/program.md)
  A struct representing the structure of an ML Program model.

- [MLModelStructure.unsupported](mlmodelstructure-swift.enum/unsupported.md)
  Represents an unsupported model.

### Loading a model structure

- [load(asset:)](mlmodelstructure-swift.enum/load(asset:).md)
  Load the model structure asynchronously from the model asset.

- [load(contentsOf:)](mlmodelstructure-swift.enum/load(contentsof:).md)
  Load the model structure asynchronously given the location of its on-disk representation.

## See Also

### Compute plan

- [MLComputePlan](mlcomputeplan-1w21n.md)
  A class representing the compute plan of a model.

- [MLComputePolicy](mlcomputepolicy.md)
  The compute policy determining what compute device, or compute devices, to execute ML workloads on.

- [withMLTensorComputePolicy(_:_:)](withmltensorcomputepolicy(_:_:)-8stx9.md)
  Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.

- [withMLTensorComputePolicy(_:_:)](withmltensorcomputepolicy(_:_:)-6z33x.md)
  Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
