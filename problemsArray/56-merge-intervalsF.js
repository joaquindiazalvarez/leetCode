/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
 var merge = function(intervals){
    intervals.sort(function(a, b){return a[0]- b[0]})
    for(let i = 0; i < intervals.length; i++){
        if(i <= intervals.length - 2 && intervals[i][1] >= intervals[i + 1][0] && intervals[i][1] < intervals[i+1][1]){
            intervals[i] = [intervals[i][0], intervals[i + 1][1]]
            for(let j = i + 1; j < intervals.length; j++){
                intervals[j] = intervals[j + 1]
            } 
            intervals.length--
            i--
        }
        else if(i <= intervals.length - 2 && intervals[i][0] === intervals[i + 1][0] && intervals[i][1] === intervals[i+1][1]){
            for(let j = i + 1; j < intervals.length; j++){
                intervals[j] = intervals[j + 1];
            }
            intervals.length--
            i--
        }
        else if(i <= intervals.length - 2 && intervals[i][1] >= intervals[i + 1][0] && intervals[i][1] >= intervals[i+1][1]){
            for(let j = i + 1; j < intervals.length; j++){
                intervals[j] = intervals[j + 1];
            }
            intervals.length--
            i--
        }
    }
    return intervals
    
};
console.log(merge([[1,4],[0,2],[3,5]]))