#set xrange [0:30]
set terminal pngcairo enhanced color lw 1 size 1000, 700 font 'Arial-Bold'
#set output "throughput_1000mbps_nooutliers.png"
set output "throughput_1000mbps.png"

#set xlabel "Time (Seconds)" font ",18"
set ylabel "througput (Mbits/sec)" font ",18"
set key outside;
#set key right top;

set style fill solid 0.25 
set style boxplot nooutliers pointtype 7
set style data boxplot
set boxwidth 0.5 absolute
#set boxwidth 0.5
#set pointsize 0.5

set xtics ("TCP" 2, "UDP" 6) scale 0.0
set xtics nomirror
set ytics nomirror
set title 'Throughput comparison for TCP and UDP at 1000 Mbps Bandwidth'

set yrange [340:1000]

plot "1000mbps.txt" using (1):1 lc rgb 'red' title "FdEmu",\
	 "" using (2):2 lc rgb 'green' title "Netmap", \
	 "" using (3):3 lc rgb 'blue' title "Dpdk", \
	 "" using (5):4 lc rgb 'blue' notitle, \
	 "" using (6):5 lc rgb 'green' notitle,\
	 "" using (7):6 lc rgb 'red' notitle 
