from conans import ConanFile, CMake, tools


class WjwwoodserialConan(ConanFile):
    name = "wjwwood-serial"
    version = "1.2.2"
    license = "MIT"
    author = "Kevin Lannen kevin.lannen@gmail.com"
    url = "github.com/kevswims/serial"
    description = "Cross platform serial port library"
    topics = ("Serial", "RS232")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "*"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("*serial.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["serial"]

