#version 120
#extension GL_ARB_explicit_attrib_location : enable

layout(location = 0) in vec3 positions;
layout(location = 1) in vec2 vTexCoord;
layout(location = 2) in vec4 vTexOffset;
layout(location = 3) in vec3 vTint;

varying vec2 fTexCoord;
varying vec4 fTexOffset;
varying vec3 fTint;

uniform mat4 transformation_matrix;

void main(){
    gl_Position = transformation_matrix * vec4(positions, 1.0);
    fTexCoord = vTexCoord;
    fTexOffset = vTexOffset;
    fTint = vTint;
}