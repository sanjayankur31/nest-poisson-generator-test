set term pngcairo font "OpenSans, 28" size 1920,1028
set title "Rasters of spike trains generated from a poisson generator in Nest"

set yrange[0:11]
set ytics 1,1,11

set xlabel "Time (ms)"
set ylabel "Neurons"

set output "raster.png"
plot for [i=12:21] 'spike_detector-'.i.'-0.gdf' using 2:($1-1) title '' with points ls 1
