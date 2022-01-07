# linux-src-port-hash-distribution-fix
micro-demo about fixing linux's port distribution

The issue: Linux changed to use even and odd ports depending on whether connect() or bind() was called

See https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=07f4c90062f8fc7c8c26f8f95324cbe8fa3145a5

For naive implementations of mapping source ports to something else (e.g., a load balancer's CPU cores) this can cause uneven distribution which can severely cripple performance. 

For a "better" fix that works in a wider range, you could implement perhaps a LCG to evenly map an unevenly distributed set of input integers to an evenly distributed output range, *roughly*, see https://en.m.wikipedia.org/wiki/Linear_congruential_generator

However, for the linux problem, given that the least significant bit of a port number in Linux *only* really indicates whether it was creates with bind() or connect(), this example shows how the distribution corrects if you discard the least significant bit.

