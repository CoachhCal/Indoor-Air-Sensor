<script setup>

import Graphed from '@/components/Graphed.vue'
import Insights from '@/components/Insights.vue'
import MetricSelect from '@/components/MetricSelect.vue'

</script>


<template>

    <div class="container">

        <div class="metric">
            <MetricSelect/>
        </div>

        <div class="graph">
            <Graphed/>
            <Insights/>
        </div>

    </div>

</template>

<style>

.container {
    @apply flex flex-row mt-5 h-[90vh];
}

.metric{
    @apply flex min-w-[100px] h-full
}

.graph {
    @apply flex flex-col w-[80%]
}
</style>