package java_demo

/**
 * a_b_c_d_e_f_g_h_i
 * a b c d e f g h i
 * Created by intel on 2018/3/16.
 */
fun main(args: Array<String>) {
    args.flatMap {
        it.split("_")
    }.map {
        print("$it ")
    }
}