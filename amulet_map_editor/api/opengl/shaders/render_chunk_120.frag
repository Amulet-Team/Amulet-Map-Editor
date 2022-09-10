#version 120
varying vec2 fTexCoord;
varying vec4 fTexOffset;
varying vec3 fTint;

uniform sampler2D image;

void main(){
    vec4 texColor = texture2D(
    	image,
    	vec2(
			mix(fTexOffset.x, fTexOffset.z, mod(fTexCoord.x, 1.0)),
			mix(fTexOffset.y, fTexOffset.w, mod(fTexCoord.y, 1.0))
		)
	);
	if(texColor.a < 0.02)
        discard;
    texColor.xyz = texColor.xyz * fTint * 0.85;
	gl_FragColor = texColor;
}