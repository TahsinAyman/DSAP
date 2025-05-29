cmake_minimum_required(VERSION 4.0.2)
project(app)

include_directories(src/include)

file(GLOB LIB_SOURCES "src/lib/*.cpp")
add_executable(main.out src/main.cpp ${LIB_SOURCES})

add_library(${PROJECT_NAME} STATIC ${LIB_SOURCES})

install(TARGETS ${PROJECT_NAME} ARCHIVE DESTINATION lib)
install(DIRECTORY src/include/ DESTINATION include)
install(DIRECTORY resources/ DESTINATION resources)