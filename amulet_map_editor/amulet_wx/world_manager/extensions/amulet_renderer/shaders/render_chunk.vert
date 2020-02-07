# version 330
in layout(location = 0) vec3 positions;
in layout(location = 1) vec2 vTexCoord;
in layout(location = 2) vec4 vTexOffset;

out vec2 fTexCoord;
out vec4 fTexOffset;

uniform mat4 transformation_matrix;

void main(){
    gl_Position = transformation_matrix * vec4(positions, 1.0);
    fTexCoord = vTexCoord;
    fTexOffset = vTexOffset;
}