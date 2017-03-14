module.exports = function(grunt){
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        responsive_images: {
            dev: {
                options: {engine: 'gm'},
                sizes: [{
                    name: 'xsmall', width: 150
                },{
                    name: 'small', width: 320
                },{
                    name: 'medium', width: 640
                },{
                    name: 'large', width: 1024
                }],
                files: [{
                    expand: true,
                    src: ['**/*.{jpg,gif,png}'],
                    cwd: 'images',
                    dest: 'new-responsive-imgs',
                }]
            }
        },

        copy: {
            dev: {
                files: [{
                    expand: true,
                    src:['images'],
                    cwd: 'build-portfolio-website/',
                    dest: 'new-responsive-imgs',
                }]
            }
        }
    });

    grunt.loadNpmTasks('grunt-responsive-images');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.registerTask('default', ['copy','responsive_images']);
};