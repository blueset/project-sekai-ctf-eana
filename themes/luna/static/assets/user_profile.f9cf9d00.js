import{m as r}from"./module.esm.860ebcbd.js";import{c as i,C as o,e as n}from"./base.9def3074.js";import{g as l}from"./userscore.c5e46586.js";import"./duration.c050dc80.js";import"./echarts.4cc66d9c.js";import"./notificationCounter.4f4e1e9f.js";import"./scoreboard.a9375541.js";window.Alpine=r;r.data("UserGraphs",()=>({solves:{data:[]},fails:{data:[]},awards:{data:[]},solveCount:0,failCount:0,awardCount:0,getSolvePercentage(){let t=this.solveCount/(this.solveCount+this.failCount)*100;return Math.round(t)},getFailPercentage(){let t=this.failCount/(this.solveCount+this.failCount)*100;return Math.round(t)},getCategoryBreakdown(){let t=[],e={};this.solves.data.map(s=>{t.push(s.challenge.category)}),t.forEach(s=>{s in e?e[s]+=1:e[s]=1});let a=[];for(const s in e)a.push({name:s,count:e[s],percent:e[s]/t.length*100,color:i(s)});return a},async init(){const t=window.USER?window.USER.id:"me";this.solves=await o.pages.users.userSolves(t),this.fails=await o.pages.users.userFails(t),this.awards=await o.pages.users.userAwards(t),this.solveCount=this.solves.meta.count,this.failCount=this.fails.meta.count,this.awardCount=this.awards.meta.count,console.log(this.solves.data);const e=window.USER||o.user;let a=l(e.id,e.name,this.solves.data,this.awards.data);this.$refs.scoregraph&&n(this.$refs.scoregraph,a)}}));r.start();