# version 330
in layout(location = 0) vec3 positions;
in layout(location = 1) vec3 colors;
out vec3 newColor;
uniform mat4 transformation_matrix;
void main(){
    gl_Position = transformation_matrix * vec4(positions, 1.0);
    newColor = colors;
}