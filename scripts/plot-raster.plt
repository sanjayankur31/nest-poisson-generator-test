set term pngcairo font "OpenSans, 28" size 1920,1028
set title "Rasters of two spike trains generated from a poisson generator in Nest"

set yrange[0:3]
set ytics 1,1,2

set xlabel "Time (ms)"
set ylabel "Neurons"

set output "raster.png"
plot "spike_detector-4-0.gdf" using 2:($1-1) title "Train 1", "spike_detector-5-0.gdf" using 2:($1-1) title "Train 2"
