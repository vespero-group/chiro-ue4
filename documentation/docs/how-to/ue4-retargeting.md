# Retarget Unreal Engine 4 Mannequin animation

This article explains how to retarget Mannequin-compatible animation for a Skeletal Mesh
with Mannequin-compatible skeleton (armature).

The entire process happens only in Unreal Engine 4 and implies you have done FBX export
with a mannequin-compatible character (perhaps following another How-To).


!!! Warning
    This article is not a part of the official Unreal Engine 4 documentation and may not be
    up to date with its latest features.


[TOC]


## Intro

This article is an example of a retargeting procedure and does not contain
the optimal retargeting settings. Every Skeletal Mesh is unique and may require different
retargeting settings for achieving better results. Do not take the advice given here
as the best possible for your project.


## 1. Import FBX

Create a separate folder for the character and import the FBX file with default settings.

<video controls width="700">
  <source src="../img/ue4-retargeting/step1-import.webm" type="video/webm">
  Step 1: Import FBX
</video>

---

## 2. Select Rig for Mannequin

We need the retargeting system to pick up Mannequin animation blueprints as a potential source of retargeting.
For that, you may need to assign the humanoid rig to the Mannequin Skeleton.

  1. Find and Open the Mannequin Skeleton asset
  2. Open the Retarget Manager
  3. Select Humanoid Rig
  4. Save the Mannequin Skeleton

<video controls width="700">
  <source src="../img/ue4-retargeting/step2-retarget-mannequin.webm" type="video/webm">
  Step 2: Select Rig for Mannequin
</video>

---

## 3. Retarget your character

  1. Find and Open your character skeleton asset
  2. Open the Retarget Manager
  3. Select Humanoid Rig
  4. Open Skeleton Tree
  5. Select "Show Retargeting Options" in the dropdown
  6. Recursively set Translation Retargeting Skeleton for all bones
  7. Set Translation Retargeting Animation for **root**
  8. Set Translation Retargeting Animation Scaled for **pelvis**
  9. Save the skeleton

<video controls width="700">
  <source src="../img/ue4-retargeting/step3-retarget-leonard.webm" type="video/webm">
  Step 3: Retarget your character
</video>

---

## 4. Retarget the animation blueprint

  1. Find the animation blueprint you want to retarget
  2. Choose the correct retargeting options
  3. Retarget and save the resulting assets

<video controls width="700">
  <source src="../img/ue4-retargeting/step4-retarget-animation.webm" type="video/webm">
  Step 4: Retarget the animation blueprint
</video>

---

## 5. Use your character and animation on the player pawn

  1. Swap skeletal mesh with your character
  2. Choose your retargeted animation blueprint as the Anim Class

<video controls width="700">
  <source src="../img/ue4-retargeting/step5-choose-leonard.webm" type="video/webm">
  Step 5: Use your character and animation on the player pawn
</video>

---

## Conclusion

As the result, we can reuse the existing animation blueprints made for the Mannequin.  

<video controls width="700">
  <source src="../img/ue4-retargeting/step6-the-result.webm" type="video/webm">
  Step 6: The result
</video>