# version 330
in vec2 fTexCoord;
in vec4 fTexOffset;
in float fTint;

out vec4 outColor;

uniform sampler2D image;

void main(){
    vec4 texColor = texture(
    	image,
    	vec2(
			mix(fTexOffset.x, fTexOffset.z, mod(fTexCoord.x, 1.0)),
			mix(fTexOffset.y, fTexOffset.w, 1.0-mod(fTexCoord.y, 1.0))
		)
	);
	if(texColor.a < 0.02)
        discard;
    if(fTint > 0.1)
    	texColor.xyz = texColor.xyz * vec3(0.0, 1.0, 0.0);
    texColor.xyz = texColor.xyz * 0.85;
	outColor = texColor;
}