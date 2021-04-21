/*
 Highcharts JS v9.0.1 (2021-02-15)

 ColorAxis module

 (c) 2012-2021 Pawel Potaczek

 License: www.highcharts.com/license
*/
(function(a){"object"===typeof module&&module.exports?(a["default"]=a,module.exports=a):"function"===typeof define&&define.amd?define("highcharts/modules/color-axis",["highcharts"],function(n){a(n);a.Highcharts=n;return a}):a("undefined"!==typeof Highcharts?Highcharts:void 0)})(function(a){function n(a,g,p,q){a.hasOwnProperty(g)||(a[g]=q.apply(null,p))}a=a?a._modules:{};n(a,"Mixins/ColorSeries.js",[],function(){return{colorPointMixin:{setVisible:function(a){var g=this,p=a?"show":"hide";g.visible=
g.options.visible=!!a;["graphic","dataLabel"].forEach(function(a){if(g[a])g[a][p]()});this.series.buildKDTree()}},colorSeriesMixin:{optionalAxis:"colorAxis",colorAxis:0,translateColors:function(){var a=this,g=this.options.nullColor,p=this.colorAxis,q=this.colorKey;(this.data.length?this.data:this.points).forEach(function(k){var r=k.getNestedProperty(q);(r=k.options.color||(k.isNull||null===k.value?g:p&&"undefined"!==typeof r?p.toColor(r,k):k.color||a.color))&&k.color!==r&&(k.color=r,"point"===a.options.legendType&&
k.legendItem&&a.chart.legend.colorizeItem(k,k.visible))})}}}});n(a,"Core/Axis/ColorAxis.js",[a["Core/Axis/Axis.js"],a["Core/Chart/Chart.js"],a["Core/Color/Color.js"],a["Mixins/ColorSeries.js"],a["Core/Animation/Fx.js"],a["Core/Globals.js"],a["Core/Legend.js"],a["Mixins/LegendSymbol.js"],a["Core/Color/Palette.js"],a["Core/Series/Point.js"],a["Core/Series/Series.js"],a["Core/Utilities.js"]],function(a,g,p,q,k,r,n,D,z,E,w,t){var F=this&&this.__extends||function(){var a=function(c,b){a=Object.setPrototypeOf||
{__proto__:[]}instanceof Array&&function(b,f){b.__proto__=f}||function(b,f){for(var d in f)f.hasOwnProperty(d)&&(b[d]=f[d])};return a(c,b)};return function(c,b){function d(){this.constructor=c}a(c,b);c.prototype=null===b?Object.create(b):(d.prototype=b.prototype,new d)}}(),x=p.parse;p=q.colorPointMixin;q=q.colorSeriesMixin;var G=r.noop,u=t.addEvent,B=t.erase,A=t.extend,H=t.isNumber,C=t.merge,v=t.pick,I=t.splat;"";A(w.prototype,q);A(E.prototype,p);g.prototype.collectionsWithUpdate.push("colorAxis");
g.prototype.collectionsWithInit.colorAxis=[g.prototype.addColorAxis];var y=function(a){function c(b,d){var f=a.call(this,b,d)||this;f.beforePadding=!1;f.chart=void 0;f.coll="colorAxis";f.dataClasses=void 0;f.legendItem=void 0;f.legendItems=void 0;f.name="";f.options=void 0;f.stops=void 0;f.visible=!0;f.init(b,d);return f}F(c,a);c.prototype.init=function(b,d){var f=b.options.legend||{},e=d.layout?"vertical"!==d.layout:"vertical"!==f.layout;f=C(c.defaultOptions,d,{showEmpty:!1,title:null,visible:f.enabled&&
(d?!1!==d.visible:!0)});this.coll="colorAxis";this.side=d.side||e?2:1;this.reversed=d.reversed||!e;this.opposite=!e;b.options[this.coll]=f;a.prototype.init.call(this,b,f);d.dataClasses&&this.initDataClasses(d);this.initStops();this.horiz=e;this.zoomEnabled=!1};c.prototype.initDataClasses=function(b){var d=this.chart,f,e=0,a=d.options.chart.colorCount,c=this.options,h=b.dataClasses.length;this.dataClasses=f=[];this.legendItems=[];b.dataClasses.forEach(function(b,m){b=C(b);f.push(b);if(d.styledMode||
!b.color)"category"===c.dataClassColor?(d.styledMode||(m=d.options.colors,a=m.length,b.color=m[e]),b.colorIndex=e,e++,e===a&&(e=0)):b.color=x(c.minColor).tweenTo(x(c.maxColor),2>h?.5:m/(h-1))})};c.prototype.hasData=function(){return!!(this.tickPositions||[]).length};c.prototype.setTickPositions=function(){if(!this.dataClasses)return a.prototype.setTickPositions.call(this)};c.prototype.initStops=function(){this.stops=this.options.stops||[[0,this.options.minColor],[1,this.options.maxColor]];this.stops.forEach(function(b){b.color=
x(b[1])})};c.prototype.setOptions=function(b){a.prototype.setOptions.call(this,b);this.options.crosshair=this.options.marker};c.prototype.setAxisSize=function(){var b=this.legendSymbol,d=this.chart,f=d.options.legend||{},e,a;b?(this.left=f=b.attr("x"),this.top=e=b.attr("y"),this.width=a=b.attr("width"),this.height=b=b.attr("height"),this.right=d.chartWidth-f-a,this.bottom=d.chartHeight-e-b,this.len=this.horiz?a:b,this.pos=this.horiz?f:e):this.len=(this.horiz?f.symbolWidth:f.symbolHeight)||c.defaultLegendLength};
c.prototype.normalizedValue=function(b){this.logarithmic&&(b=this.logarithmic.log2lin(b));return 1-(this.max-b)/(this.max-this.min||1)};c.prototype.toColor=function(b,d){var f=this.dataClasses,e=this.stops,a;if(f)for(a=f.length;a--;){var c=f[a];var h=c.from;e=c.to;if(("undefined"===typeof h||b>=h)&&("undefined"===typeof e||b<=e)){var l=c.color;d&&(d.dataClass=a,d.colorIndex=c.colorIndex);break}}else{b=this.normalizedValue(b);for(a=e.length;a--&&!(b>e[a][0]););h=e[a]||e[a+1];e=e[a+1]||h;b=1-(e[0]-
b)/(e[0]-h[0]||1);l=h.color.tweenTo(e.color,b)}return l};c.prototype.getOffset=function(){var b=this.legendGroup,d=this.chart.axisOffset[this.side];b&&(this.axisParent=b,a.prototype.getOffset.call(this),this.added||(this.added=!0,this.labelLeft=0,this.labelRight=this.width),this.chart.axisOffset[this.side]=d)};c.prototype.setLegendColor=function(){var b=this.reversed,d=b?1:0;b=b?0:1;d=this.horiz?[d,0,b,0]:[0,b,0,d];this.legendColor={linearGradient:{x1:d[0],y1:d[1],x2:d[2],y2:d[3]},stops:this.stops}};
c.prototype.drawLegendSymbol=function(b,d){var a=b.padding,e=b.options,m=this.horiz,l=v(e.symbolWidth,m?c.defaultLegendLength:12),h=v(e.symbolHeight,m?12:c.defaultLegendLength),g=v(e.labelPadding,m?16:30);e=v(e.itemDistance,10);this.setLegendColor();d.legendSymbol=this.chart.renderer.rect(0,b.baseline-11,l,h).attr({zIndex:1}).add(d.legendGroup);this.legendItemWidth=l+a+(m?e:g);this.legendItemHeight=h+a+(m?g:0)};c.prototype.setState=function(b){this.series.forEach(function(d){d.setState(b)})};c.prototype.setVisible=
function(){};c.prototype.getSeriesExtremes=function(){var b=this.series,d=b.length,a;this.dataMin=Infinity;for(this.dataMax=-Infinity;d--;){var e=b[d];var c=e.colorKey=v(e.options.colorKey,e.colorKey,e.pointValKey,e.zoneAxis,"y");var l=e.pointArrayMap;var h=e[c+"Min"]&&e[c+"Max"];if(e[c+"Data"])var g=e[c+"Data"];else if(l){g=[];l=l.indexOf(c);var k=e.yData;if(0<=l&&k)for(a=0;a<k.length;a++)g.push(v(k[a][l],k[a]))}else g=e.yData;h?(e.minColorValue=e[c+"Min"],e.maxColorValue=e[c+"Max"]):(g=w.prototype.getExtremes.call(e,
g),e.minColorValue=g.dataMin,e.maxColorValue=g.dataMax);"undefined"!==typeof e.minColorValue&&(this.dataMin=Math.min(this.dataMin,e.minColorValue),this.dataMax=Math.max(this.dataMax,e.maxColorValue));h||w.prototype.applyExtremes.call(e)}};c.prototype.drawCrosshair=function(b,d){var c=d&&d.plotX,e=d&&d.plotY,l=this.pos,g=this.len;if(d){var h=this.toPixels(d.getNestedProperty(d.series.colorKey));h<l?h=l-2:h>l+g&&(h=l+g+2);d.plotX=h;d.plotY=this.len-h;a.prototype.drawCrosshair.call(this,b,d);d.plotX=
c;d.plotY=e;this.cross&&!this.cross.addedToColorAxis&&this.legendGroup&&(this.cross.addClass("highcharts-coloraxis-marker").add(this.legendGroup),this.cross.addedToColorAxis=!0,!this.chart.styledMode&&this.crosshair&&this.cross.attr({fill:this.crosshair.color}))}};c.prototype.getPlotLinePath=function(b){var d=this.left,c=b.translatedValue,e=this.top;return H(c)?this.horiz?[["M",c-4,e-6],["L",c+4,e-6],["L",c,e],["Z"]]:[["M",d,c],["L",d-6,c+6],["L",d-6,c-6],["Z"]]:a.prototype.getPlotLinePath.call(this,
b)};c.prototype.update=function(b,d){var c=this.chart.legend;this.series.forEach(function(b){b.isDirtyData=!0});(b.dataClasses&&c.allItems||this.dataClasses)&&this.destroyItems();a.prototype.update.call(this,b,d);this.legendItem&&(this.setLegendColor(),c.colorizeItem(this,!0))};c.prototype.destroyItems=function(){var b=this.chart;this.legendItem?b.legend.destroyItem(this):this.legendItems&&this.legendItems.forEach(function(a){b.legend.destroyItem(a)});b.isDirtyLegend=!0};c.prototype.destroy=function(){this.chart.isDirtyLegend=
!0;this.destroyItems();a.prototype.destroy.apply(this,[].slice.call(arguments))};c.prototype.remove=function(b){this.destroyItems();a.prototype.remove.call(this,b)};c.prototype.getDataClassLegendSymbols=function(){var b=this,a=b.chart,c=b.legendItems,e=a.options.legend,l=e.valueDecimals,g=e.valueSuffix||"",h;c.length||b.dataClasses.forEach(function(d,e){var f=!0,k=d.from,m=d.to,n=a.numberFormatter;h="";"undefined"===typeof k?h="< ":"undefined"===typeof m&&(h="> ");"undefined"!==typeof k&&(h+=n(k,
l)+g);"undefined"!==typeof k&&"undefined"!==typeof m&&(h+=" - ");"undefined"!==typeof m&&(h+=n(m,l)+g);c.push(A({chart:a,name:h,options:{},drawLegendSymbol:D.drawRectangle,visible:!0,setState:G,isDataClass:!0,setVisible:function(){f=b.visible=!f;b.series.forEach(function(b){b.points.forEach(function(b){b.dataClass===e&&b.setVisible(f)})});a.legend.colorizeItem(this,f)}},d))});return c};c.defaultLegendLength=200;c.defaultOptions={lineWidth:0,minPadding:0,maxPadding:0,gridLineWidth:1,tickPixelInterval:72,
startOnTick:!0,endOnTick:!0,offset:0,marker:{animation:{duration:50},width:.01,color:z.neutralColor40},labels:{overflow:"justify",rotation:0},minColor:z.highlightColor10,maxColor:z.highlightColor100,tickLength:5,showInLegend:!0};c.keepProps=["legendGroup","legendItemHeight","legendItemWidth","legendItem","legendSymbol"];return c}(a);Array.prototype.push.apply(a.keepProps,y.keepProps);r.ColorAxis=y;["fill","stroke"].forEach(function(a){k.prototype[a+"Setter"]=function(){this.elem.attr(a,x(this.start).tweenTo(x(this.end),
this.pos),null,!0)}});u(g,"afterGetAxes",function(){var a=this,c=a.options;this.colorAxis=[];c.colorAxis&&(c.colorAxis=I(c.colorAxis),c.colorAxis.forEach(function(b,c){b.index=c;new y(a,b)}))});u(w,"bindAxes",function(){var a=this.axisTypes;a?-1===a.indexOf("colorAxis")&&a.push("colorAxis"):this.axisTypes=["colorAxis"]});u(n,"afterGetAllItems",function(a){var c=[],b,d;(this.chart.colorAxis||[]).forEach(function(d){(b=d.options)&&b.showInLegend&&(b.dataClasses&&b.visible?c=c.concat(d.getDataClassLegendSymbols()):
b.visible&&c.push(d),d.series.forEach(function(c){if(!c.options.showInLegend||b.dataClasses)"point"===c.options.legendType?c.points.forEach(function(b){B(a.allItems,b)}):B(a.allItems,c)}))});for(d=c.length;d--;)a.allItems.unshift(c[d])});u(n,"afterColorizeItem",function(a){a.visible&&a.item.legendColor&&a.item.legendSymbol.attr({fill:a.item.legendColor})});u(n,"afterUpdate",function(){var a=this.chart.colorAxis;a&&a.forEach(function(a,b,d){a.update({},d)})});u(w,"afterTranslate",function(){(this.chart.colorAxis&&
this.chart.colorAxis.length||this.colorAttribs)&&this.translateColors()});return y});n(a,"masters/modules/coloraxis.src.js",[],function(){})});
//# sourceMappingURL=coloraxis.js.map