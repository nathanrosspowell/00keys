/*
 * Generated on 2014-12-28
 * generator-assemble v0.5.0
 * https://github.com/assemble/generator-assemble
 *
 * Copyright (c) 2014 Hariadi Hinta
 * Licensed under the MIT license.
 */

'use strict';

module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg : grunt.file.readJSON('package.json'),

    config: {
      src: 'src',
      dist: 'build',
      temp: 'temp'
    },

    wintersmith: {
      build: {},
    },

    copy: {
      meta: {
        dot: true,
        expand: true,
        cwd: 'meta',
        src: '**',
        dest: '<%= config.dist %>/'
      }
    },

    // Before generating any new files,
    // remove any previously-created files.
    clean: [
      '<%= config.dist %>/**/*.{html,xml}', 
      '<%= config.temp %>/**/*.{html,xml}' 
    ],

    'gh-pages': {
      website: {
        options: {
          base: '<%= config.dist %>/',
          branch: 'gh-pages',
          message: 'Grunt deploy <%= grunt.template.today() %>'
        },
        src: ['**']
      }
    }

  });

  grunt.loadNpmTasks('grunt-gh-pages');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-wintersmith');

  grunt.registerTask('build', [
    'clean',
    'copy',
    'wintersmith'
  ]);
  
  grunt.registerTask('default', [
    'build'
  ]);

  grunt.registerTask('deploy', [
    'default',
    'gh-pages'
  ]);

};
