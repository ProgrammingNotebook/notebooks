# Notebook: JUnit 5

---

JUnit 5 unlike the previous version of JUnit is now composed of different modules

- **JUnit Jupiter**: Is used for writing the test cases.
- **JUnit Platform**: Is used as a foundation for launching testing framework on the JVM. The platform provides a
  Console Launcher to launch the platform from the command line and the JUnit Platform Suite Engine for running a custom
  test suite using one or more test engines on the platform

### Java Requirement

JUnit 5 requires Java 8 (or higher) at runtime. However, you can still test code that has been
compiled with previous versions of the JDK.

### Setup

You can add the JUnit 5 by adding the following libraries to the `pom.xml` file in you maven project

```xml

<dependencies>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-api</artifactId>
        <version>${junit.version}</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-engine</artifactId>
        <version>${junit.version}</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```

### Writing you first JUnit 5 test

Writing a JUnit test would require you to define the class with a method that must be annotated with `@Test` annotation
from the JUnit Jupiter library `org.junit.jupiter.api.Test`.

```java
package com.programmingnotebook;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class JUnitTest {

    @Test
    void minimumRequirementForWritingATestCase() {
        Assertions.assertEquals(20, 10 + 10);
    }
}
```

This is a simple test where we're testing the equality of two numbers, the first number represents the output and the
other equation represents the actual function to be evaluated.

## Annotations

JUnit supports the following annotations for configuring the test and extending the framework.

| Annotation | Description                                                                                                                                                                                                                                                                       |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| @Test      | Denotes that a method is a test method. Unlike JUnit 4’s @Test annotation, **_this annotation does not declare any attributes_**, since test extensions in JUnit Jupiter operate based on their own dedicated annotations. Such methods are inherited unless they are overridden. |
