# Maven Reference

## Maven Commands

### Create new project
```shell
mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DarchetypeVersion=1.4 -DinteractiveMode=false
```
* `archetype:generate` - tells Maven to execute a plugin called `archetype` with a goal of `generate`
* `-DgroupId=com.mycompany.app` - this is the package name
* `-DartifactId=my-app` - this is the project name
* `-DarchetypeArtifactId=maven-archetype-quickstart` - this is a template for the project
* `-DarchetypeVersion=1.4` - this is the version of the template
* `-DinteractiveMode=false` - this tells Maven to not prompt for input

### Build project
```shell
mvn package
```
* `package` - tells Maven to execute a plugin called `package`, which will compile the code and package it into a JAR file

### Run project
```shell
java -cp target/my-app-1.0-SNAPSHOT.jar com.mycompany.app.App
```
* `-cp target/my-app-1.0-SNAPSHOT.jar` - this tells Java to look for the JAR file in given path
* `com.mycompany.app.App` - this is the fully qualified name of the class to run

### Other Maven phases
* `validate` - validate the project is correct and all necessary information is available
* `compile` - compile the source code of the project
* `test` - test the compiled source code using a suitable unit testing framework. These tests should not require the code be packaged or deployed
* `package` - take the compiled code and package it in its distributable format, such as a JAR.
* `integration` - est: process and deploy the package if necessary into an environment where integration tests can be run
* `verify` - run any checks to verify the package is valid and meets quality criteria
* `install` - install the package into the local repository, for use as a dependency in other projects locally
* `deploy` - done in an integration or release environment, copies the final package to the remote repository for sharing with other developers and projects.
* `clean` - cleans up artifacts created by prior builds