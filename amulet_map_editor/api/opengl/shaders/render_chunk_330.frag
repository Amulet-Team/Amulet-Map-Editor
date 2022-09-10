#version 330
in vec2 fTexCoord;
in vec4 fTexOffset;
in vec3 fTint;

out vec4 outColor;

uniform sampler2D image;

void main(){
    vec4 texColor = texture(
    	image,
    	vec2(
			mix(fTexOffset.x, fTexOffset.z, mod(fTexCoord.x, 1.0)),
			mix(fTexOffset.y, fTexOffset.w, mod(fTexCoord.y, 1.0))
		)
	);
	if(texColor.a < 0.02)
        discard;
    texColor.xyz = texColor.xyz * fTint * 0.85;
	outColor = texColor;
}