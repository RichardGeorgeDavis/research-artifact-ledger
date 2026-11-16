#include <assert.h>
#include <stdio.h>
#include <string.h>
#include "variations.h"

int main(void) {
    static flam3_genome g;
    static flam3_xform xf[3];
    static unsigned short table[16384];
    randctx rng = {0};
    unsigned seed;

    g.xform = xf;
    g.num_xforms = 3;
    g.final_xform_index = 2;
    for (int i = 0; i < 3; ++i) {
        xf[i].density = 1.0;
        xf[i].num_active_vars = 1;
        xf[i].varFunc[0] = VAR_LINEAR;
        xf[i].active_var_weights[0] = 1.0;
        xf[i].c[2][0] = i + 1.0;
        xf[i].vis_adjusted = 1.0;
        xf[i].julian_power = 1.0;
        xf[i].juliascope_power = 1.0;
        xf[i].wedge_julia_power = 1.0;
        xf[i].super_shape_n1 = 1.0;
    }
    assert(flam3_create_chaos_distrib(&g, -1, table) == 0);
    for (unsigned i = 0; i < 16384; ++i)
        assert(table[i] == (i >= 8192));

    for (seed = 1; seed < 1000; ++seed) {
        memset(&rng, 0, sizeof rng);
        rng.randrsl[0] = seed;
        irandinit(&rng, 1);
        randctx trace = rng;
        unsigned first = (unsigned)irand(&trace) & 16383;
        unsigned second = (unsigned)irand(&trace) & 16383;
        unsigned third = (unsigned)irand(&trace) & 16383;
        if (table[second] == table[third])
            continue;
        double off[8] = {0};
        double zero[8] = {0};
        randctx off_rng = rng, zero_rng = rng;
        g.final_xform_enable = 0;
        assert(flam3_iterate(&g, 2, 0, off, table, &off_rng) == 0);
        g.final_xform_enable = 1;
        assert(flam3_iterate(&g, 2, 0, zero, table, &zero_rng) == 0);
        assert(off[0] == zero[0] && off[0] == table[first] + 1.0);
        assert(off[4] == table[second] + 1.0);
        assert(zero[4] == table[third] + 1.0);
        assert(off[4] != zero[4]);
        printf("seed=%u bins=%u,%u,%u output_x=%.0f,%.0f vs %.0f,%.0f counters=%lu,%lu\n",
               seed, first, second, third, off[0], off[4], zero[0], zero[4],
               off_rng.randcnt, zero_rng.randcnt);
        return 0;
    }
    return 1;
}
