<script setup>

import Graphed from '@/components/Graphed.vue'
import Insights from '@/components/Insights.vue'
import MetricSelect from '@/components/MetricSelect.vue'

</script>


<template>

        <div class="parent-wrapper">

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

.parent-wrapper {
    @apply flex mt-5 flex-row h-[90vh] max-w-[2000px] justify-center mx-auto;
}

.metric{
    @apply flex min-w-[100px] h-full
}

.graph {
    @apply flex flex-col w-[80%] border-4 border-green-900 bg-black bg-opacity-70 rounded-2xl
}
</style>