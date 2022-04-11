<template>
    <div class="select">
        <div>
            <p>country:</p>
            <el-select v-model="country" placeholder="Select a country" @change="changeCountry">
                <el-option
                v-for="item in country_list"
                :key="item.value"
                :label="item.label"
                :value="item.value">
                </el-option>
            </el-select>
        </div>

        <div>
            <p>data source:</p>
            <el-select v-model="source" placeholder="Select a data source" @change="changeSource" style="width:400px">
                <el-option
                v-for="item in source_list"
                :key="item.value"
                :label="item.label"
                :value="item.value">
                </el-option>
            </el-select>
        </div>
        <div>
            <p>time period:</p>
            <el-select v-model="period" placeholder="select a time period" @change="changePeriod">
                <el-option
                v-for="item in period_list"
                :key="item.value"
                :label="item.label"
                :value="item.value">
                </el-option>
            </el-select>
        </div>
        <div>
            <p>metric:</p>
            <el-select v-model="metric" placeholder="select a metric" @change="changeMetric">
                <el-option
                v-for="item in metric_list"
                :key="item.value"
                :label="item.label"
                :value="item.value">
                </el-option>
            </el-select>
        </div>
    </div>
</template>
	
changeCountry(value){
    this.$axios.get('/country/list',{
        value:value
    }).then(res=>{
        this.country_list = res.data;
    })
},
changeSource(value){
    this.$axios.get('/source/list',{
        value:value
    }).then(res=>{
        this.source_list = res.data;
    })
},
changePeriod(value){
    this.$axios.get('/period/list',{
        value:value
    }).then(res=>{
        this.period_list = res.data;
    })
},
changeMetric(value){
    this.$axios.get('/metric/list',{
        value:value
    }).then(res=>{
        this.metric_list = res.data;
    })
}
