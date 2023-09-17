ThisBuild / version := "0.1.0-SNAPSHOT"

ThisBuild / scalaVersion := "2.13.12"

lazy val root = (project in file("."))
  .settings(
    name := "steganography",
    libraryDependencies += "com.github.scopt" %% "scopt" % "4.0.1"
  )
