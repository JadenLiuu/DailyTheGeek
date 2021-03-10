cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

add_definitions(-std=c++14)

set(CXX_FLAGS "-Wall")
set(CMAKE_CXX_FLAGS, "${CXX_FLAGS}")
set(CMAKE_BUILD_TYPE Debug) # Debug None RelWithDebInfo MinSizeRel
add_definitions("-DE2E_TEST ")

project(jumper)

include_directories(
    ${PROJECT_SOURCE_DIR}/include
    ${PROJECT_SOURCE_DIR}/
)

file(GLOB all_SRCS
    "${PROJECT_SOURCE_DIR}/include/*.h"
    "${PROJECT_SOURCE_DIR}/*.h"
    "${PROJECT_SOURCE_DIR}/*.cpp"
)

add_executable(jumper ${all_SRCS} main.cpp) ## binary file: jumper
