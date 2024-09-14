plugins {
    id("java")
}

repositories {
    mavenCentral()
}

dependencies {
    implementation("com.google.guava:guava:30.1-jre")
    testImplementation("junit:junit:4.13.2")
}

tasks.test {
    useJUnitPlatform()
}