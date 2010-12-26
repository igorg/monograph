#!/usr/bin/env python
#-*- coding:utf-8 -*-

from os.path import join, realpath

SCORES = {
    'breast-cancer': {
        'j48': (0.628055555555555, 0.467837301587302),
        'naive-bayes': (0.715426587301587, 0.208571428571429),
        'logistic': (0.66625, 0.667400793650794),
        'smo': (0.592718253968254, 0.666706349206349)
    },
    'vehicle': {
        'j48': (0.93725319458502, 0.913885247975709),
        'naive-bayes': (0.808976530870445, 0.24322513917004),
        'logistic': (0.993578884109312, 0.994197874493927),
        'smo': (0.944338942307692, 0.996511576417004)
    },
    'hepatitis': {
        'j48': (0.696554487179487, 0.671118233618234),
        'naive-bayes': (0.859188034188034, 0.224893162393162),
        'logistic': (0.809241452991453, 0.798824786324786),
        'smo': (0.751282051282051, 0.815224358974359)
    },
    'glass': {
        'j48': (0.903216374269006, 0.837719298245614),
        'naive-bayes': (0.94083820662768, 0.17270955165692),
        'logistic': (0.959649122807017, 0.97037037037037),
        'smo': (0.891812865497076, 0.957115009746589)
    },
    'yeast': {
        'j48': (0.489176688251619, 0.95009250693802),
        'naive-bayes': (0.828630897317299, 0.842691951896392),
        'logistic': (0.858048103607771, 0.834528214616096),
        'smo': (0.773913043478261, 0.83554579093432)
    }
}

wd = realpath('.')
plot_tmpl = open(join(wd, 'gnuplot.config'), 'r').read()

for database, dictionary in SCORES.items():
    for classifier, score in dictionary.items():
        print('Gnuplot configuration for: %s - %s\n' % (database, classifier))
        cls_mean, ranking_mean = score

        tmpl_data = {
            'database': database,
            'classifier': classifier,
            'cls_mean': cls_mean,
            'ranking_mean': ranking_mean
        }

        plot_config = open(join(wd, database, classifier+'.gplot'), 'w')
        plot_config.write(plot_tmpl % tmpl_data)
        plot_config.close()
