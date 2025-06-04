cmake_minimum_required(VERSION 3.10)
project(app)

include_directories(src/include)
include_directories(src/lib)

file(GLOB LIB_SOURCES "src/lib/*.cpp")
add_executable(main.out src/main.cpp)

add_library(${PROJECT_NAME} STATIC 
  src/lib/arraylist_impl.cpp
  src/lib/linkedlist_impl.cpp
)
target_link_libraries(main.out PRIVATE app)
target_include_directories(app PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

install(TARGETS ${PROJECT_NAME} ARCHIVE DESTINATION lib)
install(DIRECTORY src/include/ DESTINATION include)
