# Skin a mesh with Mannequin armature

The article explains how to skin a humanoid character with a Mannequin-compatible armature (skeleton).
That will allow reuse of Mannequin animations for the character via animation retargeting in Unreal Engine 4.

!!! Disclaimer
    This article purpose is to demonstrate the features of Chiro add-on for Blender.
    To achieve best results, you must do more than we cover in here.
    We do not correct weight paints nor set up morph targets. That is out of scope for this tutorial.


[TOC]


## Intro

In this article we will skin a character mesh with a mannequin-compatible armature. 

The mesh proportions are not matching the Mannequin, so we will change the bones
and later use retargeting manager in Unreal Engine 4 to make the animation work.
The mesh does not have armature, vertex groups and weight paints.

Here is the character we will be skinning

<video controls width="700">
  <source src="../img/leah/intro-leah-overview.webm" type="video/webm">
</video>


---

## 1. Add Armature

The first step is to add the armature we'll be working with. To do that, find the menu and
the armature to the scene. It will be easier to work if we make it show up "In Front", so let's
do it straight away.

 1. `Add -> Armature -> Chiro (UE4 Mannequin) -> A-Pose`
 2. `Armature sidebar -> Viewport Display -> In Front`

!!! Info
    It does not matter if you start with the armature in A-Pose or T-Pose.  
    In this example we start with A-Pose merely because it's closer to the mesh posture.

<video controls width="700">
  <source src="../img/leah/step01-add-armature.webm" type="video/webm">
</video>

---

## 2. Scale Armature

Now we scale the armature so its spine length following the torso size accordingly.  
Here are a couple guidelines you could follow to make it right

  1. pelvis root should be at the top of the groin
  2. clavicle bone tails should be just in the middle of the character shoulders

!!! Warning
    If you cannot find good alignment, then don't align clavicles, just make sure
    pelvis is in the correct position. In the following steps we will adjust all the bones one by one
    anyway, but it is important to begin with the pelvis in the right spot.


<video controls width="700">
  <source src="../img/leah/step02-scale-armature.webm" type="video/webm">
</video>

---

## 3. Adjust pelvis position

Now we shall adjust the bone positions. However, pelvis is the root for all the other bones
and it is **important** that we begin with it first.  
To find the correct position for pelvis, you could follow these guidelines.

  - front view: top of the groin, middle of the mesh
  - side view: middle of the mesh, middle of glutes
  - rear view: middle of glutes, middle of the mesh

To make it easier, in this step we will move pelvis into a separate layer,
so the other bones don't obscure the view. To do that, we are switching to the `Edit Mode`.
Then, we return to the `Object Mode` and adjust the pelvis position by dragging the armature around.


<video controls width="700">
  <source src="../img/leah/step03-adjust-pelvis.webm" type="video/webm">
</video>

---

## 4. Adjust pelvis tail

The rest of the bones we will adjust in `Pose mode`.  
Now we are correcting `spine_01` position by following these guidelines

  - front view: just below navel
  - side view: middle of the mesh
  - rear view: just above the pelvis

Since the bones are connected, to adjust `spine_01` position we will update the `pelvis` bone instead.
In `Pose Mode` we will rotate `pelvis` and increase its `Scale Y`.


<video controls width="700">
  <source src="../img/leah/step04-adjust-spine01.webm" type="video/webm">
</video>

---

## 5. Adjust spine_01

Same here. To adjust `spine_02` we will update `spine_01` in `Pose Mode`. Rotate the bone and
update its `Scale Y` to change the bone length.  
Here are the guidelines for `spine_02` adjustments

  - front view: celiac plexus (aka solar plexus), just below the ribcage, top of the abdomen
  - side view: middle of the mesh

To do this, we will move the `spine_01` bone to the current layer via `Edit Mode`


<video controls width="700">
  <source src="../img/leah/step05-adjust-spine02.webm" type="video/webm">
</video>

---

## 6. Adjust spine_02

Repeating the same proceduce to adjust `spine_03` position.  
The guidelines

  - front view: middle of the chest
  - side view: middle of the mesh, below the bottom of armpit, following the shape of the mesh

!!! Info
    To move the bone into current layer we're using shortcuts (`Shift-M` and `M`).
    If you're not comfortable with shortcuts, you could repeat the UI actions from the previous steps.
    The shortcuts are doing the same thing.

<video controls width="700">
  <source src="../img/leah/step06-adjust-spine03.webm" type="video/webm">
</video>

---

## 7. Adjust neck and head

Repeating the procedure for `neck` and `head` bones.

`neck root` guidelines:

  - front view: root of the neck, above clavicles
  - side view: root of the neck, just above the shoulders

`neck tail` guidelines:

  - side view: behind the jaw, below the ear

`head` guidelines:

  - parallel to face


<video controls width="700">
  <source src="../img/leah/step07-neck-head.webm" type="video/webm">
</video>

---

## 8. Adjust clavicles

The clavicle bones are the most error prone in retargeting Mannequin animations.
Most likely you won't be able to find the correct position for your character from the first try.
The shoulders may look broken, or positioned weirdly. To mitigate that effect,
find a correct spot for clavicle bone roots. Although, for now, we are going to leave it "as is".

!!! Info
    Later we may use the "auto-detection" provided by the addon via
    [Snap clavicles to Mannequin position](../edit-armature.md#snap-clavicles-to-mannequin-position) transformation.
    It won't give you the best possible result, but it is "good enough" to begin with.

The guidelines

  - turn on X-mirror
  - do not change clavicle root position
  - clavicle tail should be placed in the middle of the shoulder joint


<video controls width="700">
  <source src="../img/leah/step08-clavicles.webm" type="video/webm">
</video>

---

## 9. Left Arm

Following the procedure, we're leaving X-mirror turned on and update the left arm bones.  
Here are some simple guidelines for that

  - all bones should be placed in the middle of the mesh
  - `upperarm_l tail` should be placed exactly at the elbow joint
  - `lowerarm_l tail` should be placed exactly at the wrist joint
  - `hand_l tail` should be placed at the root of the middle finger


<video controls width="700">
  <source src="../img/leah/step09-left-arm.webm" type="video/webm">
</video>

---

## 10. Fingers

Skin the fingers right is tricky. Although, if you're careful enough, the result should be good.  
Here are the guidelines for you:

  - roll `hand_l` bone to find the correct `thumb to pinky` position
  - drag roots of gingers, place them to match knuckles
  - rotate the rest finger bones to find correct finger positions
  - scale the bones to match finger phalanges
  - make sure X axis of every bone except thumb looks the same way as the palm

We are still using X-mirror and only dealing with the left hand.

<video controls width="700">
  <source src="../img/leah/step10-fingers.webm" type="video/webm">
</video>

---

## 11. Left leg

Now we're ready to proceed with legs.  
The guidelines are:

  - `thigh_l root` should be already in a good position, so we don't touch it
  - `thigh_l tail` should be placed in the knee joint
  - `calf_l tail` should be placed at the ankle joint
  - `foot_l tail` should be placed at the beginning of the toes
  - `ball_l` should be aligned straight forward

We're still using X-mirror and only adjust left leg bones.  
In the process we're also using [Select Bone Group: Twist Bones](../select-bone-group.md#twist-bones)
to select all twist bones and move them into a different layer, so they don't obscure the view.

<video controls width="700">
  <source src="../img/leah/step11-left-leg.webm" type="video/webm">
</video>

---

## 12. Adjust the right side

Ideally the mesh will by symmetrical along the X axis. However, the world is not ideal, so we
should account for the differences between the left and right sides of the mesh.

  1. Turn OFF X-mirror
  2. Correct right arm, palm, fingers and leg

<video controls width="700">
  <source src="../img/leah/step12-right-side.webm" type="video/webm">
</video>

---

## 13. Apply the pose as Rest Pose

We have the armature in the correct pose precisely following the mesh posture and proportions.  
Now we need to apply all our changes to the armature by applying the pose as Rest Pose.

<video controls width="700">
  <source src="../img/leah/step13-apply-pose.webm" type="video/webm">
</video>

---

## 14. Parent the armature

It is time to parent the mesh with the armature. Ideally you may like to amend the
weight paints for the vertex groups, but for the brevity of this tutorial we will
use auto-weights and leave it as is. This will give us good enough result for now.

<video controls width="700">
  <source src="../img/leah/step14-parent.webm" type="video/webm">
</video>

---

## 15. T-Pose

A requirement for the armature to be mannequin-compatible is correct bone rolls.  
The Chiro add-on has built-in functionality to correct the rolls. However, to do so properly
it needs the character to be in T-Pose. Thus, we will put our mesh into T-Pose now.

Here are the guidelines

  - Face: looking straight forward, head is aligned by Z axis
  - Feet: looking straight forward, parallel to the floor
  - Arms: aligned by X axis, parallel to the floor
  - Upper arms: parallel to the floor
  - Elbows: looking straight back (towards Y axis)
  - Palms: parallel to the floor

<video controls width="700">
  <source src="../img/leah/step15-tpose.webm" type="video/webm">
</video>

---

## 16. Apply the pose to mesh

Before we move on, we need to put the mesh into the new T pose at rest. To do so, we will use
[Apply Pose to Mesh & as Rest](../apply-pose-to-mesh.md) feature. Without it, the mesh will
keep its original form and not the T-Pose we've just made for it.

`Pose -> Apply -> Apply Pose to Mesh & as Rest (Chiro)`

<video controls width="700">
  <source src="../img/leah/step16-apply-to-mesh.webm" type="video/webm">
</video>

---

## 16.5. (Optional) Snap clavicles

This step is optional, because it may have different results depending on the character. Sometimes it may help
with shoulders, sometimes it would make things worse. You should try both ways and choose the best option
that suits your character anatomy.

!!! Info
    If you are skinning your character for the first time, we are recommending to skip this step
    and come back later to try this option if you find that your character shoulders aren't looking
    properly.  
    We also encourage you to save the progress you've made so far in a separate blend file, so
    you could come back to this step later and rework not from the very beginning, but from this step.

To do that we will use [Snap clavicles to Mannequin position](../edit-armature.md#snap-clavicles-to-mannequin-position)
transformation.

Find and press in the menu:

 * `Armature -> Chiro (UE4) -> Mannequin --> Snap clavicles to Mannequin position`

<video controls width="700">
  <source src="../img/leah/step165-snap-clavicles.webm" type="video/webm">
</video>

---

## 17. Fix bone rolls

Now we should be able to correct the bone rolls via the [Bone Roll T-Pose](../edit-armature.md#bone-roll-t-pose) transformation.  

  2. Switch to `Edit Mode`
  2. `Armature -> Chiro (UE4) -> Mannequin --> Bone Roll T-Pose`

<video controls width="700">
  <source src="../img/leah/step17-bone-reroll.webm" type="video/webm">
</video>

---

## 18. Fix feet rotation

The [Bone Roll T-Pose](../edit-armature.md#bone-roll-t-pose) transformation will try to detect the best
rotation. However, depending on the actual mesh pose, it will not be correct for some bones. Particularly,
if the feet of the mesh don't look straight forward, the roll may be incorrect.

Not a big problem. We can fix the rolls manually.
To do that:

  - Make sure X-Mirror is turned OFF
  - fix the **left foot** roll so **X axis** looks **down**
  - fix the **right foot** roll so **X axis** looks **up**

!!! Warning
    If your mesh has asymmetry, X-mirror will dislocate the bones, this is why we turn it off

!!! Info
    In this video, we're hiding the obstructive bones by selecting them and pressing `H` on keyboard.
    To unhide them later you can press `Alt+H`.

<video controls width="700">
  <source src="../img/leah/step18-fix-feet-rotation.webm" type="video/webm">
</video>

---

## 19. A-Pose

The final step before it's ready for exporting. The add-on [Export FBX](../export-fbx.md) operator
relies on the armature to be in A-Pose to correct the bone rotations and make it compatible with
the Mannequin armature. Thus, the last step before exporting is to pose it into A-Pose and apply
it to the mesh. Similar to what we did with T-Pose before.

  1. Go to `Pose mode`
  2. Find and press in menu `Pose -> Re-Pose (Chiro UE4) -> "Mannequin --> A-Pose"`
  3. Find and press in menu `Pose -> Apply -> Apply Pose to Mesh & as Rest (Chiro)`

<video controls width="700">
  <source src="../img/leah/step19-apose.webm" type="video/webm">
</video>

---

## 20. Export FBX

Now it is ready for exporting to FBX. However, the add-on has its own [Export FBX](../export-fbx.md) operator,
that uses correct export settings and takes care about some extra stuff that you rarely want to do manually.
For more details on the Export FBX operator, see its own documentation section.

!!! Note
    Export FBX operator saves files into the same folder with your current .blend file 

!!! Warning
    The export may take some time. Wait until the dropdown disappears from the screen.

!!! Info
    If the proportions of your character are exactly the same as Mannequin (e.g. you did not update any bone scales,
    only rotations), you might import it with the Mannequin skeleton and reuse animations with no retargeting required.
    If the proportions are different, you will need retargeting.

 * `File -> Export -> FBX (Chiro UE4 Mannequin) -> Save as ***.fbx`

<video controls width="700">
  <source src="../img/leah/step20-export.webm" type="video/webm">
  Step 10: Export to FBX
</video>

---

## Conclusion

The resulting FBX file is ready for use in Unreal Engine 4 with default import settings.  
Although, most likely it will need animation retargeting in Unreal Engine 4.
If you are not sure how to do that, read [HowTo: UE4 Retargeting](ue4-retargeting.md).


# Results

!!! Warning
    These results are not ideal, because we did not do manual weight painting and mesh correction.  
    The goal is to show you what the add-on is capable of, not to teach how to skin characters professionaly.

### Third person

<video controls width="700">
  <source src="../img/leah/the-result-1.webm" type="video/webm">
  The result
</video>

---

### Advanced Locomotion System v4

<video controls width="700">
  <source src="../img/leah/the-result-2.webm" type="video/webm">
  The result
</video>
