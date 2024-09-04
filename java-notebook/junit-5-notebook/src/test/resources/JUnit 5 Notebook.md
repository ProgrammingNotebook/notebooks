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