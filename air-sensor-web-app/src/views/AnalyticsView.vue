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
    @apply flex flex-col mt-[100px] h-[80vh] max-w-[2000px] justify-center items-center mx-auto  xl:flex-row
}

.metric{
    @apply flex mb-2 min-w-[100px] w-[80%] xl:h-full xl:w-fit xl:mb-0
}

.graph {
    @apply flex flex-col w-[80%] h-full border-4 border-green-900 bg-black bg-opacity-70 rounded-2xl
}

.insights-scroll-wrapper {
  @apply h-[150px] overflow-x-auto overflow-y-hidden;
}

</style>